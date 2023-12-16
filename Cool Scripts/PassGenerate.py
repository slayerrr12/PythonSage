import random
import string

# Define the characters to choose from for each category
LOWERCASE_LETTERS = string.ascii_lowercase
UPPERCASE_LETTERS = string.ascii_uppercase
DIGITS = string.digits

# Combine all characters into one pool
ALL_CHARACTERS = LOWERCASE_LETTERS + UPPERCASE_LETTERS + DIGITS

# Generate a random password of length 8
PASSWORD_LENGTH = 8
PASSWORD = ''.join(random.choice(ALL_CHARACTERS) for _ in range(PASSWORD_LENGTH))

# Print the generated password
print("Random Password:", PASSWORD)
