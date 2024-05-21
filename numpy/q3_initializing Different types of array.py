import numpy as np


#all zero matrix
a= np.zeros((2,3,5)) #makes the given shape of the arrar and makes every element zero 
print(a)


#similayly all ones
b=np.ones((4,3,5))
print(b)


# to make it what we want 
c= np.full((2,3),99,dtype='float32') #(isrst is the size),(second is the element),(third is the type)
print(c)


d=np.full_like(c,4) #makes the array of the same shape as c and assigin every elemnt with4
print(d)


e= np.random.rand(4,3,5) # insted of passing tuples we just have to pass size assign randrom numbers
print(e)


f = np.random.randint(2,70, size=(4,5))  #assigins the randrom integer value up to given range if starging point is not given it's zero
print(f)


g= np.identity(3) #specifies the identity matrix of the given size    
print(g)


h= np.array([[1,2,3,4]])   # repeat an array 
i = np.repeat(h,3 ,axis=0)
print(i)




