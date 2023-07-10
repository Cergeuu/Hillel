import csv
import json

# read csv
with open('SampleCSVFile_11kb.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# read json
with open('sample2.json', 'r') as file:
    data = json.load(file)
    pretty_data = json.dumps(data, indent=4)
    print(pretty_data)

# Арифметична операція
try:
    result = 10 / 0
except ZeroDivisionError as zde:
    print(f"Error: {zde}")

# Робота з колекцією
try:
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError as ie:
    print(f"Error: {ie}")