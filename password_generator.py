import secrets
import string


def generate_password(length=16):

    if not isinstance(length, int) or not 8 <= length <= 64:
        raise ValueError("Password length must be between 8 and 64")

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+"

    all_chars = lowercase + uppercase + digits + symbols

    # Guarantee at least one character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill remaining positions
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))

    # Securely shuffle characters
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def password_strength(length):

    if length < 10:
        return "WEAK"

    elif length < 14:
        return "DECENT"

    elif length < 18:
        return "STRONG"

    else:
        return "EXCELLENT"
