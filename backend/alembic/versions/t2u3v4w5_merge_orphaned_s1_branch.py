"""Merge orphaned s1t2u3v4 compatibility branch into main head.

Revision ID: t2u3v4w5
Revises: y1x2w3v4, s1t2u3v4
Create Date: 2026-03-18

"""

from typing import Sequence, Union

from alembic import op


revision: str = "t2u3v4w5"
down_revision: Union[str, None] = ("y1x2w3v4", "s1t2u3v4")
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
