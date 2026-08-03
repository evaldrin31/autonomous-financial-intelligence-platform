# RAG Architecture: Autonomous Financial Intelligence Platform

## Executive Summary

The Retrieval-Augmented Generation (RAG) Architecture defines how AFIP combines external knowledge sources with Large Language Models (LLMs) to provide context-aware, accurate, and grounded financial intelligence.

---

## 1. RAG System Overview

### 1.1 What is RAG?

**Retrieval-Augmented Generation** combines:
- **Retrieval**: Finding relevant context from knowledge bases
- **Augmentation**: Injecting context into prompts
- **Generation**: Using LLMs with grounded context

### 1.2 Why RAG for AFIP?

| Challenge | How RAG Helps |
|-----------|--------------|
| LLM Hallucinations | Grounds responses in retrieved facts |
| Knowledge Freshness | Real-time document updates |
| Domain Specificity | Financial documents as context |
| Cost Efficiency | Smaller prompts, less API cost |
| Explainability | Cites sources for every answer |

---

## 2. Knowledge Base

### 2.1 Document Types

| Category | Document Types | Source | Update Frequency |
|----------|---------------|--------|-------------------|
| **Regulatory** | SEC filings (10-K, 10-Q, 8-K), Prospectuses | EDGAR API | Daily |
| **Research** | Analyst reports, White papers | Vendors | Weekly |
| **News** | Financial news, Earnings transcripts | News APIs | Real-time |
| **Internal** | Strategy docs, Backtest results | User uploads | On upload |
| **Market** | Price history, Economic data | Market APIs | Real-time |
| **Academic** | Research papers, Working papers | arXiv, SSRN | Weekly |

### 2.2 Document Schema

```python
class Document(BaseModel):
    """Schema for documents in the RAG system."""
    id: UUID
    source: str
    source_type: DocumentType
    title: str
    author: Optional[str]
    publication_date: datetime
    content: str
    tickers: List[str]
    sectors: List[str]
    keywords: List[str]
    embedding_model: str
    processing_date: datetime
    status: DocumentStatus
```

---

## 3. Ingestion Pipeline

### 3.1 Pipeline Stages

1. **Document Acquisition**: Fetch from sources
2. **Document Parsing**: Extract text from PDFs
3. **Content Chunking**: Semantic segmentation
4. **Embedding Generation**: Create vectors
5. **Indexing**: Store in vector DB

### 3.2 Chunking Strategy

| Strategy | Description | Use Case |
|----------|-------------|----------|
| Fixed-size | Equal token chunks | Simple documents |
| Recursive | Hierarchical splitting | Structured documents |
| Semantic | Preserve meaning | Research papers |
| Agent-based | LLM-determined boundaries | Complex documents |

---

## 4. Retrieval Pipeline

### 4.1 Query Processing Flow

```
User Query -> Query Analysis -> Query Expansion -> Embedding -> 
Hybrid Search -> Reranking -> Top-K Chunks
```

### 4.2 Search Strategies

| Strategy | Implementation | When to Use |
|----------|----------------|-------------|
| Dense Retrieval | Vector similarity | Semantic meaning |
| Sparse Retrieval | BM25/TF-IDF | Exact keyword matches |
| Hybrid | Weighted combination | Best accuracy |
| Filtered | Metadata filtering | Constrained searches |

### 4.3 Reranking

Cross-encoder reranking for precision improvement:
- Input: Initial retrieval results
- Process: Score query-document pairs
- Output: Reranked results by relevance

---

## 5. Generation Pipeline

### 5.1 Prompt Template

```
[SYSTEM]
You are a financial assistant. Answer based ONLY on the provided context.
Cite your sources. If context is insufficient, say so clearly.

[CONTEXT]
{retrieved_documents}

[QUESTION]
{user_query}

[OUTPUT]
Answer with citations and confidence level.
```

### 5.2 Citation Format

```python
class Citation(BaseModel):
    document_id: UUID
    chunk_id: UUID
    document_title: str
    document_source: str
    excerpt: str
    relevance_score: float

class RAGResponse(BaseModel):
    answer: str
    citations: List[Citation]
    confidence: str  # High, Medium, Low
    processing_time_ms: int
```

---

## 6. Vector Database

### 6.1 pgvector Configuration

```sql
-- Enable extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Documents table
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source VARCHAR(255),
    content TEXT,
    embedding VECTOR(1536),
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- HNSW index for fast similarity search
CREATE INDEX ON documents 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
```

### 6.2 Similarity Search

```python
async def search_documents(
    query_embedding: List[float],
    top_k: int = 5,
    filters: Optional[Dict] = None
) -> List[Document]:
    """Perform similarity search with filtering."""
    query = select(Document).order_by(
        Document.embedding.cosine_distance(query_embedding)
    ).limit(top_k)
    
    if filters:
        query = apply_filters(query, filters)
    
    return await session.execute(query)
```

---

## 7. Performance Optimization

| Technique | Impact | Implementation |
|-----------|--------|----------------|
| HNSW Indexing | 100x faster search | pgvector native |
| Query Caching | 90% cache hit | Redis |
| Batch Embedding | 10x throughput | Async batching |
| Metadata Filtering | Reduced search space | PostgreSQL GIN |

---

## 8. Document Information

| Field | Value |
|-------|-------|
| Document ID | AFIP-DOC-006 |
| Version | 1.0.0 |
| Status | Draft |

---

## Next Document

**→ Continue to**: [07_Backend_Architecture.md](./07_Backend_Architecture.md)  
**← Back to**: [05_AI_Agent_Architecture.md](./05_AI_Agent_Architecture.md)
