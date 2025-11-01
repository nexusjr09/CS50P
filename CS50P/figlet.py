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
