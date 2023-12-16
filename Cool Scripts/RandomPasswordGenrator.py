import random
import string

def pass_generate(num_of_alphabets, num_of_symbols, num_of_digits, a1, a2, c, length_of_password):
    """
    Generate a random password based on the given parameters.

    Args:
        num_of_alphabets (int): Number of alphabets in the password.
        num_of_symbols (int): Number of symbols in the password.
        num_of_digits (int): Number of digits in the password.
        a1 (list): List of integers.
        a2 (list): List of alphabets.
        c (list): List of symbols.
        length_of_password (int): Length of the password.

    Returns:
        list: Generated password as a list.
    """
    password = []
    list2 = []
    list2.extend(a1 + a2 + c)  # creating a list (list2) of all integers, alphabets, and symbols
    random.shuffle(list2)  # shuffling it
    random.shuffle(a1)  # shuffling list of integers
    password.extend(a1[0:num_of_digits])
    random.shuffle(a2)  # shuffling list of alphabets
    password.extend(c[0:num_of_alphabets])
    password.extend(a2[0:num_of_symbols])
    password.extend(list2[0:(length_of_password - (num_of_alphabets + num_of_symbols + num_of_digits))])
    random.shuffle(password)
    return password


print("This is your Random password generator")

# taking the input from the user

len_of_password = int(input("HOW LONG DO YOU WANT YOUR PASSWORD TO BE: "))
no_of_digits = int(input("How many digits do you want: "))
no_of_alphabets = int(input("How many alphabets do you want in your password: "))
no_of_symbols = int(input("How many symbols do you want: "))

# getting integers, alphabets, symbols into lists
integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
a = list(string.ascii_uppercase + string.ascii_lowercase)
random.shuffle(a)
b = ['&', '@', '#', '!', '*', '%', '^']
password = []

# using join function to concatenate it all inside a string
password = pass_generate(no_of_alphabets, no_of_symbols, no_of_digits, integers, b, a, len_of_password)
password = ''.join(password)
print(password)
















