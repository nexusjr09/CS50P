import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments ")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments ")
filename = sys.argv[1]
if  not filename.endswith(".csv"):
    sys.exit("Not a CSV file")
table = []
try:
    with open(filename) as file:
        data = csv.reader(file)
        for line in data:
            table.append(line)
except FileNotFoundError:
    sys.exit("File doesnot Exits")
header = table[0]
actual = table[1:]
formated_table = tabulate(actual, headers = header,tablefmt="grid")
print(formated_table)
