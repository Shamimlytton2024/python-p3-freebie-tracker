"""create freebies table"""

Revision ID: 1212
Revises: 
Create Date: 2024-05-24 00:00:00.000000

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1212'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'freebies_py',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('item_name', sa.String(length=255), nullable=False),
        sa.Column('value', sa.Integer, nullable=False),
        sa.Column('dev_id', sa.Integer, sa.ForeignKey('devs.id'), nullable=False),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.id'), nullable=False),
    )


def downgrade():
    op.drop_table('freebies_py')
