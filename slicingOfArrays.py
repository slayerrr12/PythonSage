import numpy as np 


a1 = np.array([[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]])

print(a1[0:3,0:3])

a1 = np.array(list(range(10)))
print(a1[0:3])

a1 = np.random.randint(1,10,size=(3,3))
print(a1)

