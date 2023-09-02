# a = [1,3,2,3,1,3,1,1]

# #this will simply print all items inside the list 
# for k in a :
#     print(k)
#     print(type(k))

# this will return a key value pair and get us the result with index and thier value

# b = [[2,3,2,1],4,2,2,12,2]
# c = enumerate(b)
# for i in c :
#     if type(i[1])==list :
#         print(i[1][0])
#     else :
#         print(i[1])

c = [1,3,4,2,1,3,2]
d = list(enumerate(c))
print(d)