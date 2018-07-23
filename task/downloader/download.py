import os
import time
import threading

from sqlalchemy import func

from app_parser import db
from app_parser.domain.model import Download, Config
from app_parser.service.torrent_service import Torrent

download_pool_ids = set()


def run():
    while True:
        time.sleep(1)
        if len(download_pool_ids) >= Config.get('BT_POOL_LIMIT', int):
            continue

        if not Config.get('BT_IS_ACTIVE', bool):
            if len(download_pool_ids) == 0:
                print('Further downloads stopped via configs, all queued downloads completed')
                exit(0)
            print('Further downloads stopped via configs, downloads in queue {}'.format(len(download_pool_ids)))
            continue

        t = threading.Thread(target=download)
        t.daemon = True
        t.start()
        print('new download thread started {}'.format(t))


def download():
    d = _get_from_queue()

    if not d:
        print('no item to download')
        time.sleep(60)
        return

    try:
        download_pool_ids.add(d.id)
        d.save_path = os.path.join(Config.get('BT_DOWNLOAD_DIR'), str(int(d.search_id / 1000)), str(d.search_id))
        torrent = Torrent(d)
        torrent.download()
    except Exception as e:
        d.error = str(e)
        d.status = Download.STATUSES.index('error')
    finally:
        db.session.commit()
        download_pool_ids.remove(d.id)


def _get_from_queue() -> Download:
    return Download.query\
        .filter_by(status=Download.STATUSES.index('new'))\
        .filter(Download.id.notin_(download_pool_ids))\
        .order_by(func.rand())\
        .first()


run()
