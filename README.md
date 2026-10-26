# Password Checker

A Python command-line tool that evaluates password strength and suggests concrete improvements based on common security best practices. Input is hidden with `getpass`, so the password is never echoed or stored.

## Features

- Scores length, digits, uppercase and lowercase letters, and symbols
- Penalizes long runs of repeated characters
- Flags commonly used passwords
- Returns a score out of 8 with a Weak, Medium, or Strong rating
- Lists specific suggestions to improve the password

## Usage

```bash
git clone https://github.com/Marouane2005/password-checker.git
cd password-checker
python password_checker.py
```

Requires Python 3 and no third-party packages.

## Example

```
Password Strength Checker (input is hidden)
Enter your password:
Score: 8/8 — Strong
```

## How scoring works

| Check | Points |
| --- | --- |
| Length of 12 or more (8 or more) | 2 (1) |
| Contains a digit | 1 |
| Contains an uppercase letter | 1 |
| Contains a lowercase letter | 1 |
| Contains a symbol | 1 |
| Character variety (no long repeats) | 1 |
| Not in the common-password list | 1 |

The total is capped at 8. A score of 7 or more is Strong, 4 to 6 is Medium, and below 4 is Weak.

## License

Released under the [MIT License](LICENSE).
