"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main()
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)


def calculate_temp_cel(menu):
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print("Result: {:.2f} F".format(fahrenheit))
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
            print("Thank you.")
            choice = input(">>> ").upper()

        elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f}".format(celsius))


main()
