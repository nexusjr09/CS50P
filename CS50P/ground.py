import sys
try:
    print("Hello your name is : ", sys.argv[1])
except IndexError:
    print("ARg out of range !")