count=1
while count<=5:
    print("sumit")
    count +=1
print("loop ended")    


sumitlist= [1,2,3,4,7,5,0]
for i in sumitlist:    #for loop can also be used to traverse list,strings,tuples
    print(i)
print("loop ended")    
    
    
for i in range(5):
    print(i)
print("loop ended")

for i in range(1,10,2):   #the range(x,y,z)  where x is starting index,y is ending index, z is step
    print(i)

for i in range(len(sumitlist)):
    print(i)