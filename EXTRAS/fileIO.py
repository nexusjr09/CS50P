import csv

name = input("Enter your name: ")
home = input("Enter your home: ")

with open("names.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])
