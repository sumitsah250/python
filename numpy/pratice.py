
# print the following pattern using the functions learn to initiate the matrix

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1

import numpy as np

a=np.ones((5,5))
b=np.zeros((3,3))
b[1,1]=9
a[1:4,1:4]=b
# a[1:-1,1:-1]=b # can be done this way too

print(a)

#tip

# how to prevent the new copying variable pointing to the same address as that of original
#let's say

c=np.array([1,2,3,4])
d=c
d[1]=909
print(d)
print(c)

# output
# [  1 909   3   4]
# [  1 909   3   4]

# here the value of both the array changes regardless of changing in one
# so insted of this we use

e=np.array([1,2,3,4])
f=e.copy()
f[0]=99
print(e)
print(f)
 
#  output
# [1 2 3 4]
# [99  2  3  4]

#here we can see the output where only changed in f and not altur the values of e