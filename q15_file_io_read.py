# 'r'  open for reading(default)
# 'w'  open for writing,truncating the file first
# 'x'  create a new file and open it ffor writing
# 'a'  open for writing, apending to the end of the file if it exists
# 'b'  binary mode 
# 't'  text mode(default)
# '+'  open a disk file for updatind(reading and writing)



f = open("demo.txt","r")
# data=f.read() #reads the entire file at a time
data1=f.read(5)  #reads the word up to specified word


data2 = f.readline() #reads one line at a time
data3 = f.readline()



# print(data)
print(data1)
print(data2)   
print(data3) #once the line is read it can't be read again if we try to read returns empty file




# print(type(data))
f.close()

 