camelcase = input("Enter camelCase: ")
snake_case = ""
for i in range(len(camelcase)):
    if camelcase[i].isupper():
        snake_case = snake_case + "_" + camelcase[i].lower()
    else:
        snake_case += camelcase[i]

print(f"snake_case :{snake_case}")