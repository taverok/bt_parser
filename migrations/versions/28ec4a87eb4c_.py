"""empty message

Revision ID: 28ec4a87eb4c
Revises: a97f4e5cd38b
Create Date: 2018-07-25 14:45:58.462490

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '28ec4a87eb4c'
down_revision = 'a97f4e5cd38b'
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
               type_=sa.UnicodeText(length=4294000000),
               existing_nullable=True)
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
    op.alter_column('parsed_data', 'gender',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('parsed_data', 'magnet_link',
               existing_type=mysql.MEDIUMTEXT(),
               type_=sa.Text(length=65535),
               existing_nullable=True)
    op.alter_column('parsed_data', 'raw_page_data',
               existing_type=mysql.LONGTEXT(),
               type_=sa.UnicodeText(length=4294000000),
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
               type_=sa.UnicodeText(length=4294000000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('search', 'error',
               existing_type=sa.UnicodeText(length=4294000000),
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
               existing_type=sa.UnicodeText(length=4294000000),
               type_=mysql.LONGTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'magnet_link',
               existing_type=sa.Text(length=65535),
               type_=mysql.MEDIUMTEXT(),
               existing_nullable=True)
    op.alter_column('parsed_data', 'gender',
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
    op.alter_column('download', 'error',
               existing_type=sa.UnicodeText(length=4294000000),
               type_=mysql.LONGTEXT(),
               existing_nullable=True)
    # ### end Alembic commands ###


def upgrade_db_resource():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('resource_media', 'type',
               existing_type=mysql.ENUM('MOVIE', 'SERIES'),
               type_=sa.Enum('VIDEO', 'SUBTITLE', 'AUDIO', name='types'),
               existing_nullable=False)
    op.drop_index('ix_resource_media_file_type', table_name='resource_media')
    op.drop_column('resource_media', 'file_type')
    # ### end Alembic commands ###


def downgrade_db_resource():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resource_media', sa.Column('file_type', mysql.ENUM('VIDEO', 'SUBTITLE', 'AUDIO'), nullable=False))
    op.create_index('ix_resource_media_file_type', 'resource_media', ['file_type'], unique=False)
    op.alter_column('resource_media', 'type',
               existing_type=sa.Enum('VIDEO', 'SUBTITLE', 'AUDIO', name='types'),
               type_=mysql.ENUM('MOVIE', 'SERIES'),
               existing_nullable=False)
    # ### end Alembic commands ###
