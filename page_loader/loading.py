# _*_ coding: utf-8 _*_
import requests
import os
from page_loader.links import get_res
from page_loader.files import write_to_file
from page_loader.resources import download_resources
from page_loader.names import get_files_name


def download(url, path_for_download=os.getcwd()):
    path_to_file = os.path.join(path_for_download, get_files_name(url))
    r = requests.get(url)
    dir_for_download = os.path.splitext(path_to_file)[0] + '_files'
    resources, page = get_res(url, r.text, dir_for_download)
    write_to_file(page, path_to_file)
    os.mkdir(dir_for_download)
    if resources:
        download_resources(resources)
    return path_to_file
