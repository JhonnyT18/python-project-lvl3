import os
from urllib.parse import urlparse


def get_files_name(url_):
    something, ext = os.path.splitext(urlparse(url_).path)
    if ext:
        url, ext = os.path.splitext(url_)
    else:
        url = url_
        ext = '.html'
    parts = urlparse(url)
    parsed_url = parts.netloc + parts.path
    files_name = ''
    for i in parsed_url:
        if i.isalpha() or i.isdigit():
            files_name += i
        else:
            files_name += '-'
    files_name += ext
    return files_name
