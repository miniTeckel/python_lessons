from zeep import Client
import math


def read_price(path="./currencies.txt"):
    list_price = []
    with open(path, "rt") as source:
         for line in source:
            dest = line.split(" ")
            list_price.append((int(dest[1]), dest[2].strip()))        
    return list_price 


def convert_to_rub(price, currency):
    if currency == "RUB":
        return price
    client = Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.ConvertToNum("", currency, "RUB", price, True, "", "")


def total_price(price_list):
    result = 0
    for price in price_list:
        result += convert_to_rub(price[0], price[1])
    return result


if __name__ == "__main__":
    lst = read_price()
    print("Total price is %.0f RUB" %math.ceil(total_price(lst)))