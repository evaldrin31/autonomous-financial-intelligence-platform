import datetime
from typing import Optional, List
from sqlalchemy import String, Integer, Float, Boolean, DateTime, Text, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    role: Mapped[str] = mapped_column(String(50), default="USER", nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    portfolios: Mapped[List["Portfolio"]] = relationship("Portfolio", back_populates="user", cascade="all, delete-orphan")


class Portfolio(Base):
    __tablename__ = "portfolios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    initial_cash: Mapped[float] = mapped_column(Float, default=100000.0, nullable=False)
    current_cash: Mapped[float] = mapped_column(Float, default=100000.0, nullable=False)
    total_value: Mapped[float] = mapped_column(Float, default=100000.0, nullable=False)
    risk_tolerance: Mapped[str] = mapped_column(String(50), default="MEDIUM", nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    user: Mapped["User"] = relationship("User", back_populates="portfolios")
    holdings: Mapped[List["PortfolioHolding"]] = relationship("PortfolioHolding", back_populates="portfolio", cascade="all, delete-orphan")
    orders: Mapped[List["Order"]] = relationship("Order", back_populates="portfolio", cascade="all, delete-orphan")
    theses: Mapped[List["InvestmentThesis"]] = relationship("InvestmentThesis", back_populates="portfolio", cascade="all, delete-orphan")


class PortfolioHolding(Base):
    __tablename__ = "portfolio_holdings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    portfolio_id: Mapped[int] = mapped_column(Integer, ForeignKey("portfolios.id"), nullable=False)
    ticker: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    average_cost: Mapped[float] = mapped_column(Float, nullable=False)
    current_price: Mapped[float] = mapped_column(Float, nullable=False)
    market_value: Mapped[float] = mapped_column(Float, nullable=False)
    unrealized_pnl: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    portfolio: Mapped["Portfolio"] = relationship("Portfolio", back_populates="holdings")


class Asset(Base):
    __tablename__ = "assets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ticker: Mapped[str] = mapped_column(String(20), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    asset_type: Mapped[str] = mapped_column(String(50), default="EQUITY", nullable=False)
    sector: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    industry: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class MarketData(Base):
    __tablename__ = "market_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ticker: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime, index=True, nullable=False)
    open: Mapped[float] = mapped_column(Float, nullable=False)
    high: Mapped[float] = mapped_column(Float, nullable=False)
    low: Mapped[float] = mapped_column(Float, nullable=False)
    close: Mapped[float] = mapped_column(Float, nullable=False)
    volume: Mapped[float] = mapped_column(Float, nullable=False)
    adjusted_close: Mapped[Optional[float]] = mapped_column(Float, nullable=True)


class FundamentalData(Base):
    __tablename__ = "fundamental_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ticker: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    period_ending: Mapped[datetime.datetime] = mapped_column(DateTime, index=True, nullable=False)
    revenue: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    net_income: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    eps: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    operating_margin: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    pe_ratio: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    pb_ratio: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    debt_to_equity: Mapped[Optional[float]] = mapped_column(Float, nullable=True)


class MacroIndicator(Base):
    __tablename__ = "macro_indicators"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    series_id: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime, index=True, nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)


class NewsEvent(Base):
    __tablename__ = "news_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(500), nullable=False)
    source: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    published_at: Mapped[datetime.datetime] = mapped_column(DateTime, index=True, nullable=False)
    sentiment_score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    materiality: Mapped[str] = mapped_column(String(50), default="MEDIUM", nullable=False)
    summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


class FinancialDocument(Base):
    __tablename__ = "financial_documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ticker: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    document_type: Mapped[str] = mapped_column(String(50), nullable=False)
    filing_date: Mapped[datetime.datetime] = mapped_column(DateTime, index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    source_url: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    content_hash: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

    chunks: Mapped[List["DocumentChunk"]] = relationship("DocumentChunk", back_populates="document", cascade="all, delete-orphan")


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    document_id: Mapped[int] = mapped_column(Integer, ForeignKey("financial_documents.id"), nullable=False)
    chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    embedding_id: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)

    document: Mapped["FinancialDocument"] = relationship("FinancialDocument", back_populates="chunks")


class InvestmentThesis(Base):
    __tablename__ = "investment_theses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    portfolio_id: Mapped[int] = mapped_column(Integer, ForeignKey("portfolios.id"), nullable=False)
    ticker: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    direction: Mapped[str] = mapped_column(String(20), default="BUY", nullable=False)
    thesis_text: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="PROPOSED", nullable=False)
    confidence: Mapped[float] = mapped_column(Float, default=0.5, nullable=False)
    invalidation_conditions: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    portfolio: Mapped["Portfolio"] = relationship("Portfolio", back_populates="theses")
    opinions: Mapped[List["AgentOpinion"]] = relationship("AgentOpinion", back_populates="thesis", cascade="all, delete-orphan")


class AgentOpinion(Base):
    __tablename__ = "agent_opinions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    thesis_id: Mapped[int] = mapped_column(Integer, ForeignKey("investment_theses.id"), nullable=False)
    agent_name: Mapped[str] = mapped_column(String(100), nullable=False)
    signal: Mapped[str] = mapped_column(String(20), nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    reasoning: Mapped[str] = mapped_column(Text, nullable=False)
    supporting_evidence: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)

    thesis: Mapped["InvestmentThesis"] = relationship("InvestmentThesis", back_populates="opinions")


class Decision(Base):
    __tablename__ = "decisions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    thesis_id: Mapped[int] = mapped_column(Integer, ForeignKey("investment_theses.id"), nullable=False)
    portfolio_id: Mapped[int] = mapped_column(Integer, ForeignKey("portfolios.id"), nullable=False)
    final_signal: Mapped[str] = mapped_column(String(20), nullable=False)
    consensus_summary: Mapped[str] = mapped_column(Text, nullable=False)
    disagreements: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    portfolio_id: Mapped[int] = mapped_column(Integer, ForeignKey("portfolios.id"), nullable=False)
    decision_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("decisions.id"), nullable=True)
    ticker: Mapped[str] = mapped_column(String(20), nullable=False)
    side: Mapped[str] = mapped_column(String(10), nullable=False)
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    order_type: Mapped[str] = mapped_column(String(20), default="MARKET", nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="PENDING", nullable=False)
    requested_price: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)

    portfolio: Mapped["Portfolio"] = relationship("Portfolio", back_populates="orders")
    trades: Mapped[List["Trade"]] = relationship("Trade", back_populates="order", cascade="all, delete-orphan")


class Trade(Base):
    __tablename__ = "trades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"), nullable=False)
    execution_price: Mapped[float] = mapped_column(Float, nullable=False)
    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    commission: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    slippage: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    executed_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)

    order: Mapped["Order"] = relationship("Order", back_populates="trades")


class DataSourceHealth(Base):
    __tablename__ = "data_source_health"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    source_name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="HEALTHY", nullable=False)
    freshness_seconds: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    last_successful_update: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    error_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


class AuditEvent(Base):
    __tablename__ = "audit_events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    event_type: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    payload_json: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
