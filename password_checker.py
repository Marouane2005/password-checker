import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    strength = "Strong"

    if all(errors):
        strength = "Very Weak"
    elif length_error or sum(errors) > 2:
        strength = "Weak"
    elif sum(errors) == 1:
        strength = "Medium"

    return strength

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print("Password strength:", check_password_strength(pwd))
