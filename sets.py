numbers = [1,2,3,4,5,6,7,8]
#to initalise a set 
uniques = set(numbers)

# just like sets in maths they have unique  each eleemtn is diff

print(uniques)

# ways to initialise set 

a1 = {1,3} # with curly braces



# even if we try to initialise set and insert duplicate values in it we will have diff values
a2 = {3,3,3,3,31,1,1,1,1,2,2,2,2}
print(a2)

#adding and removing items from sets

a2.add(6)
print(a2)

print(a1&a2)


