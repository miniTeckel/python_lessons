from zeep import Client
import math

CLIENT = Client('http://www.webservicex.net/length.asmx?WSDL')

def read_file(path="./travel.txt"):
    list_price = []
    with open(path, "rt") as source:
         for line in source:
            dest = line.split(" ")
            list_price.append((float(dest[1].replace(",", "")), dest[2].strip()))        
    return list_price 


def convert_to_km(length):
    return CLIENT.service.ChangeLengthUnit(length, "Miles", "Kilometers")


def total_distance(length_list):
    result = 0
    for length in length_list:
        result += convert_to_km(length[0])
    return result


if __name__ == "__main__":
    lst = read_file()
    print("Total distance is %.2f km" %total_distance(lst))