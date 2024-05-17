# 'r'  open for reading(default)
# 'w'  open for writing,truncating the file first ("truncating")
# 'x'  create a new file and open it ffor writing
# 'a'  open for writing, apending to the end of the file if it exists
# 'b'  binary mode 
# 't'  text mode(default)
# '+'  open a disk file for updatind(reading and writing)

# 'r+'  overwrite from begining(pointer is at beginning)
# 'w+'  read+overwrite truncates the data
# 'a+'  read+append (pointer is at end)
 
 
 #tip : every thing id done through pointers


f = open("demo.txt","r")  
data=f.read()
print(data)
f.close()

f = open("demo.txt","a") #if there is do demo file then this creates the file before performing the next work both for("w","r")
f.write("this was the change")
f.close()

f = open("demo.txt","r")
data=f.read()
print(data)
f.close()

# can be also witten ad 
with open("demo.txt","r") as f:  #similar to that of function
    data = f.read()
  
  
#any module can be installed by using pip install name_of_module in terminal (some times pip3)
#deleting files

import os
os.remove("demo.txt")  #this removes the files from the system 


 