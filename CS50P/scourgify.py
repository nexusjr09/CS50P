import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many commandLine Arguments")
if len(sys.argv) < 3:
    sys.exit("Too Few command-line arguments ")


oldfile_name = sys.argv[1]
newfile_name = sys.argv[2]
if not oldfile_name.endswith(".csv") or not newfile_name.endswith(".csv"):
    sys.exit("Invalid FileName")
with open (oldfile_name) as file:
    file_list = csv.reader(file)
    for line in file_list:
        name = line[0].strip("'")
        first_name , last_name = name.split(", ")   
        house = line[1].strip().strip("")
        print(first_name)
        print(last_name)
        print(house)   