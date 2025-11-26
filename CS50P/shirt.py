import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments ")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

rawfile = sys.argv[1].lower()
finalfile = sys.argv[2].lower()

valid_ext=(".jpeg",".png",".jpg")

if not rawfile.endswith(valid_ext):
    sys.exit("Incorrect file format of Input file")
if not finalfile.endswith(valid_ext):
    sys.exit("Incorrect file format of Output File")
in_ext = rawfile.split(".")[-1]
out_ext = finalfile.split(".")[-1]
if in_ext!=out_ext:
    sys.exit("Both the input and output file  must have same extension !")

