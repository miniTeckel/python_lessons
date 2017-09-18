#!/usr/bin/python
# -*- coding: utf8 -*-
'''
Lesson 2.2
'''

import sys
import json
import yaml
from pprint import pprint


def write_cook_book_json(cook_book, file_name):
    with open(file_name, "wt", encoding="utf8") as cb_file:
        json.dump(cook_book, cb_file, indent=2)
        #book=json.dumps(cook_book, indent=2)
        # cb_file.write(book)


def write_cook_book_yaml(cook_book, file_name):
    with open(file_name, "wt", encoding="utf8") as cb_file:
        yaml.dump(cook_book, cb_file, indent=2)


def read_cook_book_json(file_name):
    with open(file_name, "rt", encoding="utf8") as cb_file:
        return json.load(cb_file)


def read_cook_book_yaml(file_name):
    with open(file_name, "rt", encoding="utf8") as cb_file:
        return yaml.load(cb_file)


def usage():
    print("Usage lesson2_1.py path_to_cook_book")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    else:
        file_name = sys.argv[1]
        file_ext = file_name.split(".")[-1]
        if file_ext == "json":
            print("Reading JSON:")
            book1 = read_cook_book_json(file_name)
            pprint(book1)
        elif file_ext == "yaml":
            print("Reading YAML:")
            book = read_cook_book_yaml(file_name)
            pprint(book)
