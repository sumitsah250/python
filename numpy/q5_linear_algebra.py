import numpy as np

a=np.ones((2,3))
b=np.full((3,2),5)
print(a)
print(b)

print(np.matmul(a,b))  #matrix multiplication 

c=np.identity(4)
print(np.linalg.det(c))  #gives the determant of the given matrix


x = np.array([[1,2],[3,4]]) #inverse of a matrix
y = np.linalg.inv(x) 
print (x)
print (y)
print (np.dot(x,y))

