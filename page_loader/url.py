# _*_ coding: utf-8 _*_
import os
import re
from urllib.parse import urlparse, urljoin


tags = {'img': 'src', 'link': 'href', 'script': 'src'}


def to_file_name(url_):
    without_ext, ext = os.path.splitext(urlparse(url_).path)
    if ext:
        url, ext = os.path.splitext(url_)
    else:
        url = url_
        ext = '.html'
    parts = urlparse(url)
    parsed_url = parts.netloc + parts.path
    name_parts = re.split('[^a-zA-Z0-9-]+', parsed_url)
    files_name = '-'.join(name_parts) + ext
    return files_name


def is_local(block, url):
    link = block.get(tags[block.name])
    netloc1 = urlparse(url).netloc
    netloc2 = urlparse(urljoin(url, link)).netloc
    return netloc1 == netloc2
