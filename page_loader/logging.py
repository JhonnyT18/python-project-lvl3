# _*_ coding: utf-8 _*_
import logging


def set_logging():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')  # noqa: E501
