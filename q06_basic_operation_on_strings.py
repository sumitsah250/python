# str1 ="sumit"   // different ways to create strings
# str2= 'sumit'
# str3 = """this is a string """


str1= "\tthis is part1.\n\tthis is part2" #\n for next line and \t for tab
print(str1)

str2= "sumit"
str3= "is a nice boy"
str4=str2+str3
print(str4)
print(len(str4))

#slicing
print(str2[1:4]) #here index 4 is not included
print(str2[:4]) # from 0 to 4
print(str2[1:]) # 1 to last
#some basic functaion
print(str2.endswith("it")) # checks if our string ends with the given character or not
print(str2.capitalize()) # makes our string first character capital
print(str2.replace("u","m"))
print (str2.replace("it","mit")) #replace the character of word in given string
print(str2.find("u")) #returs the index where u is first time come in our program
print(str2.count("u") ) #counts how many time the letter come in to out program
