number_of_items = 0
total_price = 0
number_of_items = int(input("how many items: "))
while number_of_items < 0:
    print("invalid option")
    number_of_items = int(input("how many items: "))

for item in range(number_of_items):
    total_price += float(input("price of item"))
print("total price for {} items is ${:.2f}".format(number_of_items, total_price))
