class Mobile(object):
    def __init__(self): #Constructor or special method
        self.model='RealMe x'
    def show_model(self): #Method to call the instance variable
        print('Model',self.model)

realme=Mobile()#Calling the class
print(id(realme)) #prints the address of the object where memory is allocated
realme.show_model()