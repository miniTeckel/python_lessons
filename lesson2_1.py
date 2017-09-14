#!/usr/bin/python
# -*- coding: utf8 -*-
import sys

cook_book = {
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


def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

def write_cook_book(cook_book, file_name):
    with open(file_name, "wt", encoding="utf8") as cb:
        for dish, ingredients in cook_book.items():
            cb.write("{}\n".format(dish))
            cb.write("{}\n".format(len(ingredients)))
            for ing in ingredients:
                cb.write("{} | {} | {}\n".format(ing["ingridient_name"],
                                                ing["quantity"],
                                                ing["measure"]))

def read_recep(lines):
    i=0
    name=lines[0]
    ingredients=[]
    count=int(lines[1])
    for i in range(2, count+2):
        ingridient_name, quantity, measure=lines[i].split(" | ")
        ingr={}
        ingr["ingridient_name"]=ingridient_name
        ingr["quantity"]=int(quantity)
        ingr["measure"]=measure
        ingredients.append(ingr)

    return name, ingredients

def read_cook_book(file_name):
    cook_book={}
    with open(file_name, "rt", encoding="utf8") as cb:
        book=[line.rstrip('\n') for line in cb]
    i=0
    while i<len(book):
        name_res, list_ing=read_recep(book[i:])
        cook_book[name_res]=list_ing
        i+=len(list_ing)+2

    return cook_book

def usage():
    print("Usage lesson2_1.py path_to_cook_book")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    else:
        #write_cook_book(cook_book, sys.argv[1])
        cook_book2=read_cook_book(sys.argv[1])
        print(cook_book2)
