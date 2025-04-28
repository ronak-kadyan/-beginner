weight = input("Enter your weight:")
unit = input("kilograms or pounds (K/L)")


if unit == "K":
    result = weight * 2.205
    unit = "pounds"
    print(f"your weight is {result}.{unit}")
elif unit == "L":
    result = weight / 2.205
    unit = "kilograms"
    print(f"your weight is {result}.{unit}")
else:
    print(f"{weight} is not valid")
