# for i in range (1, 21, 2):
#     print(i, end= ' ')
# print()
#
# for i in range (0, 100, 10):
#     print(i, end= ' ')
# print()

# for i in range (20, 0, -1):
#     print(i, end= ' ')
# print()

# number_of_stars = int(input("Number of stars :"))
# print(number_of_stars * '*')

# number_of_stars = int(input("Number of stars :"))
# for i in range (1, number_of_stars + 1):
#     print(i * '*')


sales = float(input("enter sales: $"))
bonus = 0
while sales >= 0:

    if sales < 1000:
        bonus = sales * 0.1
        print(bonus)
    elif sales >= 1000:
        bonus = sales * 0.15
        print(bonus)
    sales = float(input("enter sales: $"))
