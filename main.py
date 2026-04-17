def check_password(password):
    length = len(password) >= 8
    upper = False
    digit = False

    for ch in password:
        if ch.isupper():
            upper = True
        if ch.isdigit():
            digit = True

    if length and upper and digit:
        return True
    return False


while True:
    pw = input("Enter password: ")

    if check_password(pw):
        print("Strong password!")
        break
    else:
        print("Weak password, try again.")
