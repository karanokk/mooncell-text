import json
import logging
import os
import sys
from optparse import OptionParser

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from umaster import mooncell_text

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s")


def main():
    parser = OptionParser()
    parser.add_option("-o", "--output_path", dest="output_path")
    parser.add_option("-l", "--log_file", dest="log_file")
    parser.add_option("-f", '--forceUpdate', action='store_true', dest='force_update', default=False)

    options, _ = parser.parse_args()
    output_path = options.output_path
    log_file = options.log_file
    force_update = options.force_update

    logger = logging.getLogger(__name__)

    dirty_servants = mooncell_text.dirty_servants()

    if not dirty_servants:
        if force_update:
            logger.info('Force updating.')
        else:
            logger.info('Servants no update.')
            return

    servants_dir = os.path.join(output_path, 'servants')
    _create_dir_if_not_exists(servants_dir)
    log_dir = os.path.dirname(log_file)
    _create_dir_if_not_exists(log_dir)

    info = '\n'.join(f'{name} → {revid}' for name, revid in dirty_servants.items())
    logger.info(f'Update:\n{info}')

    for servant in mooncell_text.extract_all_servants():
        filename = servant['basic_data']['name'] + '.json'
        servant_file = os.path.join(servants_dir, filename)
        with open(servant_file, 'w+') as f:
            json.dump(servant, f)

    logger.info(f'Dirty servants clear!')

    with open(log_file, 'w+') as f:
        f.write(info)


def _create_dir_if_not_exists(dirpath: str):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


if __name__ == "__main__":
    main()
