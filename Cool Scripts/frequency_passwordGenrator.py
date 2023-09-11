import random
import string
def Password_generator(length, list1, list2, list3, list4):
    password = ""
    for i in range(length):
        rand = random.randint(1, 4)  # Generate a random number between 1 and 4 (inclusive).
        if rand == 1:
            password += str(random.choice(list1))
        elif rand == 2:
            password += str(random.choice(list2))
        elif rand == 3:
            password += str(random.choice(list3))
        else:
            password += str(random.choice(list4))

    return password

list_special_symbol = ['@', '#', '|', '?']
list_digit = string.digits
list_alpha_lower = string.ascii_lowercase
list_alpha_upper = string.ascii_uppercase

print(Password_generator(8, list_alpha_upper, list_alpha_lower, list_digit, list_special_symbol))
