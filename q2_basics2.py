import numpy as np

a= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

#get specific element
print(a[1,0])  #both will give the same answer as negative counting start from back and -1,-2...
print(a[1,-7])

print(a[0,:]) #get specific row
print(a[:,0]) #get specific column


print(a[0,2:6])
print(a[0,2:6:2]) # a[row index,(starting element):(ending element):(step size)]


a[1,5]=20 #changes the value at that given index
print(a)

a[:,1]=50 #makes the all the given column element 50 in this case 2nd column elements 50
a[0,:]=50 #makes the all the given row element 50 in this case 1st row elements  50
print(a)


#similay for the 3d arrays 
