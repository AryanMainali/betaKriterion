"""Compatibility placeholder for orphaned revision ID seen in deployed DBs.

Revision ID: s1t2u3v4
Revises: q9r0s1t2
Create Date: 2026-03-18

"""

from typing import Sequence, Union

from alembic import op


revision: str = "s1t2u3v4"
down_revision: Union[str, None] = "q9r0s1t2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Placeholder only: keeps historical DBs with this revision connected to the graph.
    pass


def downgrade() -> None:
    pass
