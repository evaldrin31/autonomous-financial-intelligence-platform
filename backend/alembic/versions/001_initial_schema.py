"""initial schema

Revision ID: 001_initial_schema
Revises: 
Create Date: 2026-08-09 23:45:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '001_initial_schema'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Users
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('full_name', sa.String(length=255), nullable=True),
        sa.Column('role', sa.String(length=50), nullable=False, server_default='USER'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)

    # Portfolios
    op.create_table(
        'portfolios',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('initial_cash', sa.Float(), nullable=False, server_default='100000.0'),
        sa.Column('current_cash', sa.Float(), nullable=False, server_default='100000.0'),
        sa.Column('total_value', sa.Float(), nullable=False, server_default='100000.0'),
        sa.Column('risk_tolerance', sa.String(length=50), nullable=False, server_default='MEDIUM'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index(op.f('ix_portfolios_id'), 'portfolios', ['id'], unique=False)

def downgrade() -> None:
    op.drop_table('portfolios')
    op.drop_table('users')
