#    *
#   ***
#  *****   
#printing this partten
num=int(input("enter the size of partten"))

for i in range(1,num+1):
    for j in range(num-i):
        print(end=" ")
    for k in range(i):
        print("*",end="")
    for l in range(i-1):
        print("*",end="")
        
    print()