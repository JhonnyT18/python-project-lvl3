import sys
from urllib.parse import urljoin
import os
import tempfile
from page_loader.loading import download
import requests_mock


with open(os.path.join(sys.path[0], 'fixtures/page_with_local_links.html'), 'r') as file:
    expected_page = file.read()


URL = 'https://test.com'
RESOURCES_LINK = urljoin(URL, 'assets/professions/nodejs.png')


def test_download():
    with open(os.path.join(sys.path[0], 'fixtures/page_with_global_links.html'), 'r') as file:
        testing_page = file.read()
    with tempfile.TemporaryDirectory() as tmpdirname:
        with requests_mock.Mocker() as m:
            m.get(URL, text=testing_page)
            m.get(RESOURCES_LINK, text=RESOURCES_LINK)
            file_path = download(URL, tmpdirname)
            with open(file_path, 'r') as file:
                page = file.read()
            assert page == expected_page
            assert len(os.listdir(tmpdirname)) == 2
            assert len(os.listdir(os.path.join(tmpdirname, 'test-com_files'))) == 1
