def main():
    min_password_length = 3
    password = get_password()
    while min_password_length >= 0:
        if len(password) >= min_password_length:
            print(len(password) * '*')
        password = get_password()


def get_password():
    password = input("Password: ")
    return password


# statements...

main()
