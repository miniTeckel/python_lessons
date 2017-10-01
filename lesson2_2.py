#!/usr/bin/python
# -*- coding: utf8 -*-
'''
Lesson 2.2
'''

import sys
import json
import yaml
from pprint import pprint


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']
                          ] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']
                          ]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)


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
            book = read_cook_book_json(file_name)
            pprint(book)
        elif file_ext == "yaml":
            print("Reading YAML:")
            book = read_cook_book_yaml(file_name)
            pprint(book)
        create_shop_list(book)