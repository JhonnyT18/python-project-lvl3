import sys
from urllib.parse import urljoin
import os
import tempfile
from page_loader import loading
import requests_mock


with open(os.path.join(sys.path[0], 'fixtures/page_with_local_links.html'), 'r') as file:
    expected_page = file.read()


URL = 'https://test.com'
RESOURCES_LINK = [urljoin(URL, 'assets/professions/nodejs.png'),
                  urljoin(URL, 'assets/application.css'),
                  urljoin(URL, 'packs/js/runtime.js')]


def test_download():
    with open(os.path.join(sys.path[0], 'fixtures/page_with_global_links.html'), 'r') as file:
        testing_page = file.read()
    with tempfile.TemporaryDirectory() as tmpdirname:
        with requests_mock.Mocker() as m:
            m.get(URL, text=testing_page)
            m.get(RESOURCES_LINK[0], text=RESOURCES_LINK[0])
            m.get(RESOURCES_LINK[1], text=RESOURCES_LINK[1])
            m.get(RESOURCES_LINK[2], text=RESOURCES_LINK[2])
            file_path = loading.download(URL, tmpdirname)
            with open(file_path, 'r') as file:
                page = file.read()
            assert page == expected_page
            assert len(os.listdir(tmpdirname)) == 2
            assert len(os.listdir(os.path.join(tmpdirname, 'test-com_files'))) == 3
