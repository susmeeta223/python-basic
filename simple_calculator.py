num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operations = input("Enter your operator(+,-,*,/,%): ")

if operations == "+" :
    result = num1 + num2
elif operations == "-" :
    result = num1 - num2
elif operations == "*" :
    result = num1 * num2
elif operations == "/" :
    result = num1 / num2
elif operations == "%" :
    result = num1 % num2
else : 
    result = "Invalid operation"

print(f"The result of {num1} {operations} {num2} is {result}")