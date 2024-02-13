import itertools
import string

def brute_force_attack(password):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    attempts = 0

    for length in range(1, len(password) + 1):
        for combination in itertools.product(chars, repeat=length):
            attempt = ''.join(combination)
            attempts += 1

            if attempt == password:
                return attempt, attempts

    return None, attempts

# Usage Example
encrypted_password = "2b4e8c9a16b2f4d6"
password, attempts = brute_force_attack(encrypted_password)

if password is not None:
    print(f"Password found: {password}")
    print(f"Total attempts: {attempts}")
else:
    print("Password not found.")