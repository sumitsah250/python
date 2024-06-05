#set is collection of he unordered items;
#Each element in the set must be unique & immutable.

# collection ={1,2,3,"sumit",5,2,6,8,7}
# print(collection)
# print(len(collection))

# collection1 ={} #this represents the empty directory
# print(type(collection1)) 
# collection2=set()#this represents the empty set
# print(type(collection1)) 


#methods in set

#sets are mutble but setelemts are immutable

collection =set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(1)
collection.add((1,2,3))
# collection.clear() #clears the set removes every item
# collection.remove(1)#removes the specific item from the set
# collection.pop()#pops random values 
collection2={1,4,6,7,8,"sumiy"}
print(collection.union(collection2))

print(collection.intersection(collection2))

print(len(collection))
print(collection)

print(collection.intersection(collection2))
