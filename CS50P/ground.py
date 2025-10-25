import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments !")
elif len(sys.argv) > 2:
    print("Too many arguments !")
else:
    print("Hey  your name is:" , sys.argv[1])