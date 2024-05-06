"""topic_id for question nullable=false

Revision ID: cce93c029566
Revises: 879741a11eab
Create Date: 2024-05-07 01:48:57.475792

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cce93c029566'
down_revision: Union[str, None] = '879741a11eab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Шаг 1: Создать новую таблицу без внешнего ключа
    op.create_table(
        'questions_new',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('question', sa.String, nullable=False),
        sa.Column('answer', sa.String, nullable=False),
        sa.Column('topic_id', sa.Integer, nullable=False)
    )
    
    # Шаг 2: Скопировать данные из старой таблицы в новую
    op.execute("INSERT INTO questions_new (id, question, answer, topic_id) SELECT id, question, answer, topic_id FROM questions")
    
    # Шаг 3: Удалить старую таблицу
    op.drop_table('questions')
    
    # Шаг 4: Создать новую таблицу с внешним ключом
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('question', sa.String, nullable=False),
        sa.Column('answer', sa.String, nullable=False),
        sa.Column('topic_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['topic_id'], ['topics.id'])
    )
    
    # Шаг 5: Скопировать данные обратно в новую таблицу
    op.execute("INSERT INTO questions (id, question, answer, topic_id) SELECT id, question, answer, topic_id FROM questions_new")
    
    # Шаг 6: Удалить старую таблицу
    op.drop_table('questions_new')

def downgrade():
    # Шаги для отката изменений
    # Создать старую таблицу без внешнего ключа
    op.create_table(
        'questions_old',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('question', sa.String, nullable=False),
        sa.Column('answer', sa.String, nullable=False),
        sa.Column('topic_id', sa.Integer, nullable=True)
    )
    
    # Скопировать данные из новой таблицы в старую
    op.execute("INSERT INTO questions_old (id, question, answer, topic_id) SELECT id, question, answer, topic_id FROM questions")
    
    # Удалить новую таблицу
    op.drop_table('questions')
    
    # Переименовать старую таблицу
    op.rename_table('questions_old', 'questions')
