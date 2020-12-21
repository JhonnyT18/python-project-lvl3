# _*_ coding: utf-8 _*_
import requests
import os
from urllib.parse import urlparse


def get_files_name(url):
    parts = urlparse(url)
    parsed_url = parts.netloc + parts.path + parts.params + parts.fragment
    files_name = ''
    for i in parsed_url:
        if i.isalpha():
            files_name += i
        else:
            files_name += '-'
    files_name += '.html'
    return files_name


def download(url, path_for_download=os.getcwd()):
    files_name = get_files_name(url)
    result_path = os.path.join(path_for_download, files_name)
    r = requests.get(url)
    with open(result_path, 'w') as file:
        file.write(r.text)
    return result_path
