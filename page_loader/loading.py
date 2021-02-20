# _*_ coding: utf-8 _*_
import requests
import os
from page_loader.links import get_res_links
from page_loader.storage import save
from page_loader.url import to_file_name
import logging
from progress.bar import Bar
from page_loader.errors import SomethingWrongError


def download(url, path_for_download=os.getcwd()):
    path_to_file = os.path.join(path_for_download, to_file_name(url))
    if os.path.exists(path_to_file):
        logging.warning('File already exists, content gonna be changed.')
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as er:
        raise SomethingWrongError(f'Something'
                                  f'went wrong during downloading '
                                  f'the page!\n{er}') from er
    except PermissionError as er:
        raise SomethingWrongError(f"Not enough rights for access\n{er}")
    dir_for_download = os.path.splitext(path_to_file)[0] + '_files'
    resources, page = get_res_links(url, r.text, dir_for_download)
    save(page, path_to_file)
    logging.info(f"'{url}' is downloaded into '{path_to_file}'")
    download_resources(resources, dir_for_download)
    return path_to_file


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
