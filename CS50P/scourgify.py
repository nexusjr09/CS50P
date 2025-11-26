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
try:
    with open(before,"r") as infile, open(after,"w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        writer.writerow(["first","last","house"])
        for student in reader:
            last,first = student["name"].split(", ")
            house = student["house"]
            writer.writerow([first, last, house])
except FileNotFoundError:
    sys.exit("File Doesn't exist")


