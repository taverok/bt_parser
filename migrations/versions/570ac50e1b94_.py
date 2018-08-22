"""empty message

Revision ID: 570ac50e1b94
Revises: 0362f51f9a0e
Create Date: 2018-08-21 14:43:10.017045

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '570ac50e1b94'
down_revision = '0362f51f9a0e'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('download', 'error',
               existing_type=mysql.LONGTEXT(),
               type_=sa.Text(length=16000000),
               existing_nullable=True)
    op.alter_column('download', 'files',
               existing_type=mysql.LONGTEXT(),
               type_=sa.Text(length=16000000),
               existing_nullable=True)
    op.drop_constraint('download_ibfk_2', 'download', type_='foreignkey')
    op.drop_column('download', 'search_id')
    op.alter_column('parsed_data', 'audio_info',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('parsed_data', 'casting',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('parsed_data', 'description',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('parsed_data', 'genre',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('parsed_data', 'magnet_link',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('parsed_data', 'raw_page_data',
               existing_type=mysql.LONGTEXT(),
               type_=sa.Text(length=16000000),
               existing_nullable=True)
    op.alter_column('parsed_data', 'title',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('parsed_data', 'video_info',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('search', 'error',
               existing_type=mysql.LONGTEXT(),
               type_=sa.Text(length=16000000),
               existing_nullable=True)
    op.alter_column('search', 'raw',
               existing_type=mysql.LONGTEXT(),
               type_=sa.Text(length=16000000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('search', 'raw',
               existing_type=sa.Text(length=16000000),
               type_=mysql.LONGTEXT(),
               existing_nullable=True)
    op.alter_column('search', 'error',
               existing_type=sa.Text(length=16000000),
               type_=mysql.LONGTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'video_info',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'title',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'raw_page_data',
               existing_type=sa.Text(length=16000000),
               type_=mysql.LONGTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'magnet_link',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'genre',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'description',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'casting',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'audio_info',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.add_column('download', sa.Column('search_id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False))
    op.create_foreign_key('download_ibfk_2', 'download', 'search', ['search_id'], ['id'])
    op.alter_column('download', 'files',
               existing_type=sa.Text(length=16000000),
               type_=mysql.LONGTEXT(),
               existing_nullable=True)
    op.alter_column('download', 'error',
               existing_type=sa.Text(length=16000000),
               type_=mysql.LONGTEXT(),
               existing_nullable=True)
    # ### end Alembic commands ###


def upgrade_db_resource():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('episode', 'description',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('episode', 'genre',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('episode', 'translation',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade_db_resource():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('episode', 'translation',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.alter_column('episode', 'genre',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.alter_column('episode', 'description',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    # ### end Alembic commands ###
