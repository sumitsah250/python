# N=int(input())      #dsa pratice question
# l=[]
# num=0
# for i in range(0,N):
#     num=int(input())
#     l.append(num)
N=int(input())
s=input()
l=[]
for i in range(0,len(s)):
    if(s[i] != " " ):
        l.append(int(s[i]))
        print(int(s[i]))
     

l.sort()
sum=0
ans=0
for i in range(0,len(l)):
    if(len(l)>1):
        sum=l[0]+l[1]
        ans=sum+ans
        l.remove(l[1])
        l.remove(l[0])
        l.append(sum)
        l.sort()
print(ans)

# N=int(input())
# s=input()
# l=[]
# ans=0
# if(0<N and N<pow(10,5)):
#     for i in range(0,2*N-1):
#         if(s[i] != " " ):
#             l.append(int(s[i]))
        
#     l.sort()
#     sum=0
   
#     for i in range(0,len(l)):
#         if(len(l)>1):
#             l.sort()
#             sum=l[0]+l[1]
#             ans=sum+ans
#             l.remove(l[0])
#             l.remove(l[0])
#             l.append(sum)
#             l.sort()
#     print(ans)
    

