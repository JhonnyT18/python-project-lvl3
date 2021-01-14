import os
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from page_loader.names import get_files_name


def get_res(url, page, dir_for_download):
    dir_for_download, dir_name = os.path.split(dir_for_download)
    soup = BeautifulSoup(page, 'html.parser')
    blocks = filter(lambda x: is_local_res(x, url), soup.find_all('img'))
    images_links = []
    for block in blocks:
        link_to_img = urljoin(url, block.get('src'))
        images_path = os.path.join(dir_name, get_files_name(link_to_img))
        block['src'] = images_path
        images_links.append((link_to_img, os.path.join(dir_for_download, images_path)))  # noqa: E501
    return images_links, soup.prettify(formatter='html5')


def is_local_res(element, url):
    link = element.get('src')
    netloc1 = urlparse(url).netloc
    netloc2 = urlparse(urljoin(url, link)).netloc
    return netloc1 == netloc2
