import numpy as np

a= np.array([1,2,3])
# a = np.array([1,2,3],dtype='int16')   # in this way we can also specify the type (for memory saving as per requirement)
print(a)
print(a.dtype)

b= np.array([[[1,2,3],[1,2,3],[1,2,3]]])
print(b)


#some basic function
print(b.ndim)  #gives us the dimenstion of the  array
print(b.shape)  #gives us n*m i.e the shape of the array
print(b.dtype)  #gives us the type and bit of array
print(b.itemsize) #gives the size of the items in bytes
print(b.size) #gives the total number of element in the array
print(b.nbytes) #gives the total size of the array in bytes 
