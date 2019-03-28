"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    print(MENU)
    choice = input(" ").upper()
    while choice!= "Q":
    if choice == "c":
        celsius = float(input("celsius: "))
        farnheight = celsius_tofahrenheit_con(celsius)
        print("results: {:.2f] C".format(farnheight))
    elif choice == "F":
        farnheight = float(input("Farnheight: "))
        celsius =farnheight_to_celsius_conversion(farnheight)
        print("result: {:.2f} C".format(celsius))
    else:
        print("invald option")
    print(MENU)

def celsius_tofahrenheit_con(celsius):
    return celsius * 9.0 / 5 + 32

def farnheight_to_celsius_conversion(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()