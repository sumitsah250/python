import numpy as np

stats = np.array([[1,2,3,4] ,[8,9,6,7]])
print(stats)
print(np.min(stats))  #gives the minimum value of the given array/matrix
print(np.max(stats))   #gives the maximum value of the given array/matrix

print(np.min(stats,axis=1)) #gives the min of row
print(np.min(stats,axis=0)) #gives the min of column
print(np.sum(stats))  #sums the all numbers in the given matrix/array


print(np.sum(stats,axis=0)) #gives sum of all the columns
print(np.sum(stats,axis=1)) #gives sum of all the rows

