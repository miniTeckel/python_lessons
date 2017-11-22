#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import argparse
import requests
import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--id', help='user ID')
    group.add_argument('--username', help='user name')
    parser.add_argument('--file', default='groups.json', help='resulting file')
    args = parser.parse_args()

    print (args) 