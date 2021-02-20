import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from page_loader.url import to_file_name, tags, is_local


def get_res_links(url, page, dir_for_download):
    dir_for_download, dir_name = os.path.split(dir_for_download)
    soup = BeautifulSoup(page, 'html.parser')
    blocks = filter(lambda x: is_local(x, url), soup.find_all(list(tags)))
    res_links = []
    for block in blocks:
        link_to_res = urljoin(url, block.get(tags[block.name]))
        path_to_res = os.path.join(dir_name, to_file_name(link_to_res))
        block[tags[block.name]] = path_to_res
        res_links.append((link_to_res,
                          os.path.join(dir_for_download, path_to_res)))
    return res_links, soup.prettify(formatter='html5')
