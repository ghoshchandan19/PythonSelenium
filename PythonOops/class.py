class Mobile(object):
    def __init__(self):
        self.model='RealMe x'
    def show_model(self):
        print('Model',self.model)

realme=Mobile()#Calling the class
print(id(realme)) #prints the address of the object where memory is allocated
realme.show_model()