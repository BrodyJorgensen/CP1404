import random
number_per_line = 6
min = 1
max = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Must be > 0")
        number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(number_per_line):
            number = random.randint(min, max)
            while number in quick_pick:
                number = random.randint(min, max)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
