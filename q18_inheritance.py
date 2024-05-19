class car:
    serialnumber="99"
    def __init__(self,type):
        self.type=type
    
    wheels =4
    def serial_change(self,serial):
        self.serialnumber=serial         #this only changes the value for the object which was created
        # car.serialnumber =serial       # this changes the actual value of the class
    
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class tesla(car):        # for multiple in heritance use both the calss names in ()seprated by comma
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()

car1 =tesla("model334","electric")
car2=tesla("sumit","petrol")

print(car1.name)
print(car1.type)
car1.start()
car2.stop()