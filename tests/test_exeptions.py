import pytest
import requests
import tempfile
import requests_mock
from page_loader.loading import download
import os


URL = 'https://www.test.com'


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        with tempfile.TemporaryDirectory() as tmpdirname:
            with requests_mock.Mocker() as m:
                m.get(URL, text='test')
                download(URL, os.path.join(tmpdirname, 'something'))

