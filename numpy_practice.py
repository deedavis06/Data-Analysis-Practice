
import numpy as np 

#create 2D array
A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

#create same array using arange() and reshape()
B = np.arange(1,10).reshape(3,3)

#change row 2 to all 10's
B[2] = 10
#add 5 to all elements
B+= 5
#summary statistics
array_sum = B.sum()
array_mean = B.mean()
array_std = B.std()
array_var = B.var()

#make an array of elements >= 10
gr_ten = B[B >=10]


