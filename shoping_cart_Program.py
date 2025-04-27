#shoping cart Program

item = input("what item would you like to by?:")
price = float(input("what is the price?:"))
quantity = int(input("how much do you want?:"))
total = price * quantity
print(f"your item is {item} X {quantity}")
print(f"it will cost you ${total}")
