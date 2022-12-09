import random
import string

# funtion to generate the password
def pass_generate(num_of_alphabets, num_of_symbols, num_of_digits, a1, a2, c, length_of_password):
    password = []
    list2 = []
    list2.extend(a1 + a2 + c) # creating a list (list2) of all integrs alphabets and symbols
    random.shuffle(list2) # shuffling it
    random.shuffle(a1) # shufflung list of integers
    password.extend(a1[0:num_of_digits])
    random.shuffle(a2) # shufflung list of alphabets
    password.extend(c[0:num_of_alphabets])
    password.extend(a2[0:num_of_symbols]) 
    password.extend(list2[0:(length_of_password - (num_of_alphabets + num_of_symbols + num_of_digits))])
    random.shuffle(password)
    return password


print("This is your Random password generator")

# taking the input from the user

len_of_password = int(input("HOW LONG DO YOU WANT YOUR PASSWORD TO BE :"))

no_of_digits = int(input("how many digits do you want:  "))
no_of_alphabets = int(input("how many aplhabets do you want in your password: "))
no_of_symbols = int(input("how many symbols do you want:  "))

# getting integers , alphabets , symbols into lists
integers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
a = list(string.ascii_uppercase + string.ascii_lowercase)
random.shuffle(a)
b = ['&', '@', '#', '!', '*', '%', '^']
u = ""

# using join function to concatinate it all inside a string 
u = u.join(pass_generate(no_of_alphabets, no_of_symbols, no_of_digits, integers, b, a, len_of_password))
print(u)
















