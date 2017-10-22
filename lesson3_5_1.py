from zeep import Client


def read_temperature(path="./temps.txt"):
    list_fahrenheit = []
    with open(path, "rt") as source:
         for line in source:
            fahrenheit = int(line.split(" ")[0])
            list_fahrenheit.append(fahrenheit)
    return list_fahrenheit 

def average(lst):
    sum = 0
    for i in lst:
        sum += i  
    return sum / len(lst)

def convert_temperature(fahrenheit):
    client = Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(fahrenheit, 'degreeFahrenheit', 'degreeCelsius')


if __name__ == "__main__":
    lst = read_temperature()
    fahrenheit = average(lst)
    print("%.2f" %convert_temperature(fahrenheit))