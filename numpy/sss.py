i=int(input().strip())
w=[]
while i.count(' ')<4:
    w.append(i)
    i=input().split()
w.extend(i.split(' '))
print(w)

