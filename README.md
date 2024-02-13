# Password Cracking Script

This password cracking script demonstrates basic password cracking techniques such as brute-forcing and dictionary attacks. It is intended for educational and ethical purposes only. The script attempts to crack an encrypted password by generating all possible combinations of characters and comparing them to the encrypted password.

## Author
Author: Sathvik Shetty

## Usage
To use the password cracking script, follow the steps below:

1. Ensure you have Python installed on your system.
2. Clone or download the script from the GitHub repository.
3. Open the script in your preferred Python editor or IDE.
4. Modify the `encrypted_password` variable to the target password's encrypted form.
5. Run the script.

## Functionality
The script utilizes a brute-force attack to crack the password. It iteratively generates all possible combinations of lowercase letters, uppercase letters, and digits. The script checks each generated combination against the encrypted password until a match is found or all combinations are exhausted.

## Requirements
The password cracking script has the following requirements:

- Python 3.x or higher

## Example
Here's an example of how to use the password cracking script:

```python
import itertools
import string

def brute_force_attack(password):
    # Code implementation

# Usage Example
encrypted_password = "2b4e8c9a16b2f4d6"
password, attempts = brute_force_attack(encrypted_password)

if password is not None:
    print(f"Password found: {password}")
    print(f"Total attempts: {attempts}")
else:
    print("Password not found.")