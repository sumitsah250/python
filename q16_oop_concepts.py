#there exist an init constructor for every every class we made init constructor is inialize when ever class is calle


class Students:
    name ="sumit"
    
s1 = Students()
print(s1.name)


class car:
    name ="tesla"
    color ="blue"
 
s2 = car()
print("the car is "+s2.name+" and it's color is"+s2.color)
 
#////////////////////////////
 
class names:
     name="sumit"
     def __init__(self,fullname):   #self points the object created (it can be replaced with other names but in->
                                                                       #  -> general case self is written)
         self.name=fullname
         print("new element was created") 
     
#////////////////////////////    


s3=names("sumit")
print(s3.name)