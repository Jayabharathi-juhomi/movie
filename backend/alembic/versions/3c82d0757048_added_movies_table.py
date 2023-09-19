"""added movies table

Revision ID: 3c82d0757048
Revises: 2dd458174473
Create Date: 2023-09-19 14:59:03.908959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c82d0757048'
down_revision = '2dd458174473'
branch_labels = None
depends_on = None
table_name = "movies"


def upgrade():
    op.create_table(
        table_name,
        sa.Column("id", sa.dialects.postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("director", sa.String(), nullable=True),
        sa.Column(
            "user_id",
            sa.dialects.postgresql.UUID(as_uuid=True),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "t_create",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "t_update",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
            onupdate=sa.text("now()"),
        ),
        sa.Column("t_delete", sa.TIMESTAMP(timezone=True)),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title", name="movie_title_key"),
    )


def downgrade():
    op.drop_table(table_name, schema=None)
