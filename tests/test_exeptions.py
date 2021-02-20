import pytest
import tempfile
import requests_mock
from page_loader.loading import download
import os
from page_loader.errors import SomethingWrongError


URL = 'https://www.test.com'


def test_file_not_found():
    with pytest.raises(SomethingWrongError):
        with tempfile.TemporaryDirectory() as tmpdirname:
            with requests_mock.Mocker() as m:
                m.get(URL, text='test')
                download(URL, os.path.join(tmpdirname, 'something'))
