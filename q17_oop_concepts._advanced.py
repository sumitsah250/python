class names :
    name = "default"
    def __init__(self,name,password):
        self.name=name
        self.__password=password  #to make the certain variable private we use two __ before defining the variable
        #here the password becomes private 


o1=names("sumit",1234)
o2=names("aaditya",9809)


# del(o1.name) #del keyword is used to delete the properties of object or the object itself
# del(o1.password)


print(o1.name) #after deletion this shows error
# print(o2.password)  #this will show error as password is private


# another simple example including all the concepts
class person:
    __name = "default"
    def __init__(self,name):
        self.__name=name
    def __greattings(self):
        print("hello")
    def welcome(self):
        self.__greattings()
        print("i know "+self.__name+" you are a nice boy")

o3= person("sumit")
o3.welcome()