# _*_ coding: utf-8 _*_
import requests
import os
from page_loader.storage import save
import logging
from page_loader.errors import SomethingWrongError
from progress.bar import Bar


def download_resources(resources, dir_for_download):
    if resources:
        if os.path.isdir(dir_for_download):
            logging.warning(f"Directory '{dir_for_download}' "
                            f"already exists. Content can be changed.")
        else:
            os.mkdir(dir_for_download)
            logging.info(f"Directory '{dir_for_download}' is created.")
        bar = Bar('Downloading progress:\n', fill='*', suffix='%(percent)d%%',
                  max=len(resources))
        for resource in resources:
            link, path_to_file = resource
            if os.path.splitext(resource[0])[1] == '.png' or '.jpg':
                mode = 'wb'
            else:
                mode = 'w'
            try:
                save(requests.get(link).content, path_to_file, mode)
                bar.next()
            except requests.exceptions.RequestException as er:
                raise SomethingWrongError(f"Some resources didn't "
                                          f"download\n{er}") from er
            else:
                continue
        bar.finish()
        logging.debug(f"Resources are downloaded into '{dir_for_download}'")
    else:
        logging.debug('This page has no resources.')
