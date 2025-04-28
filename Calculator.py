operator = input("Enter an opreator (+ - * /):")
num1 = float(input("Enter the 1st number:"))
num2 = float(input("Enter the 2nd number:"))

if operator == "+":
    result = num1 + num2
    print(f"Your answer is:{round(result , 3)}")
elif operator == "-":
    result = num1 - num2
    print(f"Your answer is:{round(result , 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"Your answer is:{round(result , 3)}")
elif operator == "/":
    result = num1 / num2
    print(f"Your answer is:{round(result , 3)}")
else:
    print(f"{operator} not valid")

