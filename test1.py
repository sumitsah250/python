# a = int(input("enter the first number:"))
# b= int(input("enter the second number:"))
# sum=(a+b)/2
# print(sum == 2)
def fibo(n):
    if n==0 or  n==1:
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
    
a=int(input("enter the number up to which you want to print the series"))
for i in range(a):
    print(fibo(i),end=" ")
    
    
    
