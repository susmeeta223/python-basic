num1 = input("Enter your first number: ")
try: 
    num1 = float(num1)
except ValueError:
    print("Invalid input, please enter a valid number")
    exit()

num2 = input("Enter your second number: ")
try:
    num2 = float(num2)
except ValueError:
    print("Invalid input, please enter a valid number")
    exit()
operations = input("Enter your operator(+,-,*,/,%): ")

if operations == "+" :
    result = num1 + num2
elif operations == "-" :
    result = num1 - num2
elif operations == "*" :
    result = num1 * num2
elif operations == "/" :
    try:
        result = num1/num2
    except ZeroDivisionError:
        result = "error : cannot be divided by zero"
elif operations == "%" :
    try:
        result = num1 % num2
    except ZeroDivisionError:
        result = "error : cannot be modulo by zero"
else : 
    result = "Invalid operation"

print(f"The result of {num1} {operations} {num2} is {result}")