try:
   data = int(input("User's Input "))
   print(f"Data is {data}")
except ValueError:
   print("Only integer allowed ! ")