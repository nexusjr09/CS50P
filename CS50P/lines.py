import sys
import os
count = 0
try:
    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        for line in sys.argv[1]:
            line = line.strip()
            if line == "":
                continue
            if line.startswith("#"):
                continue
            else:
                count += 1 
except FileNotFoundError:
    sys.exit()
print(count)