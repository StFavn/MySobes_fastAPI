"""Add SobesModel & SobesQuestionModel

Revision ID: 7375f6f0b3d2
Revises: 3a4a4380689b
Create Date: 2024-06-16 23:43:23.633964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7375f6f0b3d2'
down_revision: Union[str, None] = '3a4a4380689b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sobeses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('average_score', sa.Float(), nullable=True),
    sa.Column('count_questions', sa.Integer(), nullable=True),
    sa.Column('create_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sobes_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sobes_id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('user_answer', sa.String(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['sobes_id'], ['sobeses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sobes_questions')
    op.drop_table('sobeses')
    # ### end Alembic commands ###
