import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_path = sys.argv[1]
if not file_path.endswith(".py"):
    sys.exit("Not a Python file")

count = 0
try:
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(count)
