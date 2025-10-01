#!/usr/bin/env python3
import re
import getpass

COMMON = {
    '123456', 'password', '12345678', 'qwerty', 'abc123',
    '111111', '1234567', 'dragon', '123123', 'baseball'
}

def score_password(pwd: str) -> (int, list):
    """Return (score 0-8, suggestions list)."""
    score = 0
    suggestions = []

    # length scoring
    if len(pwd) >= 12:
        score += 2
    elif len(pwd) >= 8:
        score += 1
    else:
        suggestions.append("Make it at least 8 characters (12+ is better).")

    # digits
    if re.search(r"\d", pwd):
        score += 1
    else:
        suggestions.append("Add digits (0-9).")

    # uppercase
    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    # lowercase
    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    # symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        score += 1
    else:
        suggestions.append("Add symbols (e.g. !@#$%).")

    # variety bonus (no repeated same characters)
    if len(set(pwd)) > len(pwd) * 0.6:
        score += 1
    else:
        suggestions.append("Avoid long runs of the same character or simple repeats.")

    # common password check
    if pwd.lower() in COMMON:
        suggestions.append("This password is commonly used — choose a unique one.")
    else:
        score += 1

    return min(score, 8), suggestions

def classify(score: int) -> str:
    if score >= 7:
        return "Strong"
    if score >= 4:
        return "Medium"
    return "Weak"

def main():
    print("Password Strength Checker (input is hidden)")
    pwd = getpass.getpass("Enter your password: ")
    if not pwd:
        print("No password entered. Exiting.")
        return

    score, suggestions = score_password(pwd)
    print(f"Score: {score}/8 — {classify(score)}")
    if suggestions:
        print("\nSuggestions to improve:")
        for s in suggestions:
            print("- " + s)

if __name__ == '__main__':
    main()
