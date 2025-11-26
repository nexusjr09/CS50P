import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many commandLine Arguments")
if len(sys.argv) < 3:
    sys.exit("Too Few command-line arguments ")
oldfile = sys.argv[1]
newfile = sys.argv[2]
if not oldfile.endswith(".csv") or not newfile.endswith(".csv"):
    sys.exit("Invalid FileName")

before = sys.argv[1]
after = sys.argv[2]
with open(before,"r") as file:
    dict_format = csv.DictReader(file)
    for student in dict_format:
        last,first = student["name"].split(", ")
        house = student["house"]
        