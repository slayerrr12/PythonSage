import random
import string

# Define the characters to choose from for each category
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits

# Combine all characters into one pool
all_characters = lowercase_letters + uppercase_letters + digits

# Generate a random password of length 8
password_length = 8
password = ''.join(random.choice(all_characters) for _ in range(password_length))

# Print the generated password
print("Random Password:",password)