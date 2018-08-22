"""empty message

Revision ID: 0362f51f9a0e
Revises: 
Create Date: 2018-08-21 13:49:02.184419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0362f51f9a0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('value', sa.String(length=2000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('search',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title_ru', sa.String(length=250), nullable=True),
    sa.Column('title_en', sa.String(length=250), nullable=True),
    sa.Column('kinopoisk_id', sa.String(length=250), nullable=True),
    sa.Column('error', sa.Text(length=16000000), nullable=True),
    sa.Column('year', sa.SmallInteger(), nullable=True),
    sa.Column('type', sa.Enum('MOVIE', 'SERIES', name='resourcetype'), nullable=False),
    sa.Column('status', sa.Enum('NEW', 'PROCESSING', 'ERROR', 'NOT_FOUND', 'COMPLETED', name='statuses'), nullable=False),
    sa.Column('import_source', sa.String(length=250), nullable=True),
    sa.Column('import_source_id', sa.String(length=250), nullable=True),
    sa.Column('raw', sa.Text(length=16000000), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('kinopoisk_id')
    )
    op.create_index(op.f('ix_search_status'), 'search', ['status'], unique=False)
    op.create_index(op.f('ix_search_type'), 'search', ['type'], unique=False)
    op.create_table('parsed_data',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('kinopoisk_id', sa.String(length=250), nullable=True),
    sa.Column('import_source_id', sa.String(length=250), nullable=True),
    sa.Column('page_link', sa.String(length=250), nullable=True),
    sa.Column('raw_page_data', sa.Text(length=16000000), nullable=True),
    sa.Column('quality', sa.String(length=250), nullable=True),
    sa.Column('format', sa.String(length=250), nullable=True),
    sa.Column('country', sa.String(length=250), nullable=True),
    sa.Column('size', sa.String(length=250), nullable=True),
    sa.Column('title', sa.Text(length=65535), nullable=True),
    sa.Column('title_ru', sa.String(length=250), nullable=True),
    sa.Column('title_en', sa.String(length=250), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('translation', sa.String(length=250), nullable=True),
    sa.Column('translation_code', sa.String(length=250), nullable=True),
    sa.Column('subtitle', sa.String(length=250), nullable=True),
    sa.Column('subtitle_format', sa.String(length=250), nullable=True),
    sa.Column('genre', sa.Text(length=65535), nullable=True),
    sa.Column('description', sa.Text(length=65535), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('casting', sa.Text(length=65535), nullable=True),
    sa.Column('video_info', sa.Text(length=65535), nullable=True),
    sa.Column('audio_info', sa.Text(length=65535), nullable=True),
    sa.Column('magnet_link', sa.Text(length=65535), nullable=True),
    sa.Column('search_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['search_id'], ['search.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('download',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('progress', sa.Float(), nullable=True),
    sa.Column('download_rate_kb', sa.Float(), nullable=True),
    sa.Column('upload_rate_kb', sa.Float(), nullable=True),
    sa.Column('total_download_kb', sa.Float(), nullable=True),
    sa.Column('num_peers', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('changed_at', sa.DateTime(), nullable=True),
    sa.Column('next_update_at', sa.DateTime(), nullable=True),
    sa.Column('downloaded_at', sa.DateTime(), nullable=True),
    sa.Column('save_path', sa.String(length=250), nullable=True),
    sa.Column('status', sa.Enum('NEW', 'UPDATED', 'DOWNLOADING', 'PAUSED', 'COMPLETED', 'ERROR', 'DECOMPOSED', name='statuses'), nullable=True),
    sa.Column('bt_state', sa.String(length=250), nullable=True),
    sa.Column('error', sa.Text(length=16000000), nullable=True),
    sa.Column('files', sa.Text(length=16000000), nullable=True),
    sa.Column('type', sa.Enum('MOVIE', 'SERIES', name='resourcetype'), nullable=False),
    sa.Column('parsed_data_id', sa.BigInteger(), nullable=False),
    sa.Column('search_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['parsed_data_id'], ['parsed_data.id'], ),
    sa.ForeignKeyConstraint(['search_id'], ['search.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_download_type'), 'download', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_download_type'), table_name='download')
    op.drop_table('download')
    op.drop_table('parsed_data')
    op.drop_index(op.f('ix_search_type'), table_name='search')
    op.drop_index(op.f('ix_search_status'), table_name='search')
    op.drop_table('search')
    op.drop_table('config')
    # ### end Alembic commands ###


def upgrade_db_resource():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('episode',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('episode_no', sa.Integer(), nullable=True),
    sa.Column('episode_title', sa.UnicodeText(), nullable=False),
    sa.Column('kinopoisk_id', sa.String(length=250), nullable=True),
    sa.Column('translation', sa.Text(length=65535), nullable=True),
    sa.Column('description', sa.Text(length=65535), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('genre', sa.Text(length=65535), nullable=True),
    sa.Column('country', sa.Text(), nullable=True),
    sa.Column('status', sa.Enum('NOT_ENCODED', 'ENCODING', 'NOT_DEPLOYED', 'READY', name='statuses'), nullable=True),
    sa.Column('type', sa.Enum('MOVIE', 'SERIES', name='resourcetype'), nullable=False),
    sa.Column('mime', sa.String(length=250), nullable=False),
    sa.Column('extension', sa.String(length=250), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.Column('system_path', sa.String(length=250), nullable=True),
    sa.Column('parent_folder', sa.String(length=250), nullable=True),
    sa.Column('parsed_data_id', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_episode_type'), 'episode', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade_db_resource():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_episode_type'), table_name='episode')
    op.drop_table('episode')
    # ### end Alembic commands ###
