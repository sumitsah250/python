
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
