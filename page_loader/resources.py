# _*_ coding: utf-8 _*_
import requests
import os
from page_loader.storage import save
import logging
from progress.bar import Bar


def download_resources(resources, dir_for_download):
    if resources:
        if os.path.isdir(dir_for_download):
            logging.warning(f"Directory '{dir_for_download}' "
                            f"already exists. Content can be changed.")
        else:
            os.mkdir(dir_for_download)
            logging.info(f"Directory '{dir_for_download}' is created.")
        bar = Bar('Downloading progress:', fill='*', suffix='%(percent)d%%',
                  max=len(resources))
        for resource in resources:
            link, path_to_file = resource
            try:
                save(requests.get(link).content, path_to_file)
                bar.next()
            except requests.exceptions.RequestException as er:
                logging.warning(f"Some resources didn't download\n{er}")
                continue
        bar.finish()
        logging.debug(f"Resources are downloaded into '{dir_for_download}'")
    else:
        logging.debug('This page has no resources.')
