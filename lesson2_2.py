#!/usr/bin/python
# -*- coding: utf8 -*-
'''
Lesson 2.2
'''

import sys
import json
from pprint import pprint

COOK_BOOK = {
    'яйчница': [
        {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
    'стейк': [
        {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
        {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
    'салат': [
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
        {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
}

def write_cook_book(cook_book, file_name):
    with open(file_name, "wt", encoding="utf8") as cb_file:
        json.dump(cook_book, cb_file, indent=2)
        #book=json.dumps(cook_book, indent=2)
        #cb_file.write(book)

def read_cook_book(file_name):
    with open(file_name, "rt", encoding="utf8") as cb_file:
        return json.load(cb_file)


def usage():
    print("Usage lesson2_1.py path_to_cook_book")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    else:
        #write_cook_book(COOK_BOOK, sys.argv[1])
        book=read_cook_book(sys.argv[1])
        pprint(book)
