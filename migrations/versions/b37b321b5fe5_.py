"""empty message

Revision ID: b37b321b5fe5
Revises: 87f2534acc37
Create Date: 2022-07-30 00:44:17.176769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b37b321b5fe5'
down_revision = '87f2534acc37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Shows', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Shows', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('Shows_venue_id_fkey', 'Shows', type_='foreignkey')
    op.drop_constraint('Shows_artist_id_fkey', 'Shows', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('Shows_artist_id_fkey', 'Shows', 'Venue', ['artist_id'], ['id'])
    op.create_foreign_key('Shows_venue_id_fkey', 'Shows', 'Venue', ['venue_id'], ['id'])
    op.alter_column('Shows', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Shows', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###