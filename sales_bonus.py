sales = float(input("enter sales: $"))
bonus = 0
if sales <1000:
    bonus = sales * 0.1
    print(bonus)
elif sales >= 1000:
    bonus  = sales * 0.15
    print (bonus)