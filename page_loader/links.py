import os
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from page_loader.names import get_files_name


tags = {'img': 'src', 'link': 'href', 'script': 'src'}


def get_res(url, page, dir_for_download):
    dir_for_download, dir_name = os.path.split(dir_for_download)
    soup = BeautifulSoup(page, 'html.parser')
    blocks = filter(lambda x: is_local_res(x, url), soup.find_all(list(tags)))
    res_links = []
    for block in blocks:
        link_to_res = urljoin(url, block.get(tags[block.name]))
        path_to_res = os.path.join(dir_name, get_files_name(link_to_res))
        block[tags[block.name]] = path_to_res
        res_links.append((link_to_res, os.path.join(dir_for_download, path_to_res)))  # noqa: E501
    return res_links, soup.prettify(formatter='html5')


def is_local_res(block, url):
    link = block.get(tags[block.name])
    netloc1 = urlparse(url).netloc
    netloc2 = urlparse(urljoin(url, link)).netloc
    return netloc1 == netloc2
