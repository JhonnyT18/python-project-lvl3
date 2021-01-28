# _*_ coding: utf-8 _*_
import logging
import sys


def set_logging():
    logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(levelname)s: %(message)s')  # noqa: E501
