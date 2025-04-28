temp = float(input("what is the temprature?:"))
unit = input("Celsius or farhrenheit?(C/F):")

if unit == "C":
    result = round((9 * temp)/5 + 32 , 2)
    unit = "farhrenheit"
    print(f"your temprature is{result}{unit}")
elif unit == "F":
    result = round((temp - 32) * 5 / 9, 2) 
    unit = "celsius"
    print(f"your temprature is: {result} {unit}")
else:
    print(f"{unit} not vaild")

