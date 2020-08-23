class Mobile(object):
    def __init__(self): #Constructor or special method
        self.model='RealMe x'


realme=Mobile()#Calling the class
print(id(realme)) #prints the address of the object where memory is allocated
realme.show_model()