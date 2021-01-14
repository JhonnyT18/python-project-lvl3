# _*_ coding: utf-8 _*_
import pytest
from page_loader.loading import get_files_name


cases = [
    (
     'https://ru.hexlet.io/courses',
     'ru-hexlet-io-courses.html'
    ),
    (
     'https://www.google.ru',
     'www-google-ru.html'
    ),
    (
     'https://klavogonki.ru/gamelist',
     'klavogonki-ru-gamelist.html'
    )
]


@pytest.mark.parametrize('url, expected', cases)
def test_get_files_name(url, expected):
    assert get_files_name(url) == expected


