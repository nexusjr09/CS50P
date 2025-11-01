import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
own = figlet.getFonts()

if len(sys.argv) == 1:
    choose = random.choice(own)
    figlet.setFont(font= choose)
    data = input("Input: ")
    print(figlet.renderText(data))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    fontname = sys.argv[2]
    if fontname not in figlet.getFonts():
        sys.exit("Invalid FontName")
    else:
        figlet.setFont(font=fontname)
        data = input("Input: ")
        print(figlet.renderText(data))
else:
    sys.exit("Invalid Format")
