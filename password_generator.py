import random
import string


def generate_password(*, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True, length=8):
    if not any([use_uppercase, use_lowercase, use_numbers, use_symbols]):
        raise ValueError(
            'At least one of the arguments must be True: use_uppercase, use_lowercase, use_numbers, use_symbols'
        )

    chars = []

    if use_uppercase:
        chars.extend(string.ascii_uppercase)
    if use_lowercase:
        chars.extend(string.ascii_lowercase)
    if use_numbers:
        chars.extend(string.digits)
    if use_symbols:
        allowed_symbols = '!@#$%^&*()_+-='
        chars.extend(allowed_symbols)

    password = ''.join(random.choice(chars) for _ in range(length))

    return password


if __name__ == '__main__':
    password_length = int(input('Enter password length: '))
    print(generate_password(length=password_length))
