# _*_ coding: utf-8 _*_
import logging
import sys


def setup():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stderr,
                        format='%(levelname)s: %(message)s')
