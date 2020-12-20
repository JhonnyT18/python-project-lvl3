# _*_ coding: utf-8 _*_
import requests
import os
from urllib.parse import urlparse


def get_files_name(url):
    o = urlparse(url)
    o1 = o.netloc + o.path + o.params + o.fragment
    result = ''
    for i in o1:
        if i.isalpha():
            result += i
        else:
            result += '-'
    result += '.html'
    return result


def download(url, path_for_download=os.getcwd()):
    files_name = get_files_name(url)
    result_path = path_for_download + '/' + files_name
    r = requests.get(url)
    with open(result_path, 'w') as file:
        file.write(r.text)
    return result_path
