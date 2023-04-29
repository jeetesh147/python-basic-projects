# Generate secure password:
import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits
    # create a list of characters for the password
    password_chars = []
    for i in range(length):
        password_chars.append(random.choice(chars))
    password = ''.join(password_chars)

    return password
password = generate_password(12)
print(password)


