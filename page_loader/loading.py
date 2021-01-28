# _*_ coding: utf-8 _*_
import requests
import os
from page_loader.links import get_res
from page_loader.files import write_to_file
from page_loader.resources import download_resources
from page_loader.names import get_files_name
import logging
from page_loader.logging import set_logging


set_logging()


def download(url, path_for_download=os.getcwd()):
    path_to_file = os.path.join(path_for_download, get_files_name(url))
    if os.path.exists(path_to_file):
        raise OSError("File already exists.")
    r = requests.get(url)
    dir_for_download = os.path.splitext(path_to_file)[0] + '_files'
    resources, page = get_res(url, r.text, dir_for_download)
    write_to_file(page, path_to_file)
    logging.info(f"'{url}' is downloaded into '{path_to_file}'")
    os.mkdir(dir_for_download)
    logging.info(f"Directory '{dir_for_download}' is created.")
    if resources:
        download_resources(resources)
        logging.info(f"Resources are downloaded into {dir_for_download}")
    return path_to_file
