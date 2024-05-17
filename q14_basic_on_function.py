def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))


n= int(input("up to what value you want to print the number"))
for i in range(n):
    print(fibo(i) ,end=" ")