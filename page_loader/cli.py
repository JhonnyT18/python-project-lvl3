#  _*_ coding: utf-8 _*_
import argparse
import os


def get_parser():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('url', type=str)
    parser.add_argument('-o', '--output', type=str,
                        help='Specify a directory for loading',
                        default=os.getcwd())
    return parser
