import os
import logging
import requests
from page_loader.url import to_file_name
from page_loader.errors import SomethingWrongError
from page_loader.links import get_res_links
from page_loader.storage import save
from page_loader.resources import download_resources


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
