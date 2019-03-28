"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "c":
            celsius = float(input("celsius: "))
            fahrenheit = celsius_to_fahrenheit_con(celsius)
            print("results: {:.2f] C".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Farnheight: "))
            celsius = fahrenheit_to_celsius_conversion(fahrenheit)
            print("result: {:.2f} C".format(celsius))
        else:
            print("invald option")
            print(MENU)


def celsius_to_fahrenheit_con(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius_conversion(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()
