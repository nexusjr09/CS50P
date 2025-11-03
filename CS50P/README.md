# CS50’s Introduction to Programming with Python — Solutions 🐍

This repository contains my solutions to the problem sets from **Harvard’s CS50P (Introduction to Programming with Python)** course.

## 📘 About
CS50P is a beginner-friendly course that covers core programming concepts using Python.  
Exercises Includes Practice of : 


- Functions and Conditionals  
- Loops  
- File I/O  
- Exceptions  
- Libraries  
- Object-Oriented Programming  
- Unit Testing  


texts = input("Enter Strings : ").strip()
toremove = ["a","e","i","o","u","A","E","I","O","U"]
clean = ""
for  i in range(len(texts)):
    if texts[i] not in toremove:
        clean = clean + texts[i]
print(clean)