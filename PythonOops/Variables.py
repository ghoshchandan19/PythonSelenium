#Instance variable
class Mobile:
    def __init__(self):
        self.model='Realme X'
    def show_model(self):
        print(self.model)

realme=Mobile()
realme.show_model()

#Accesing instance variable outside class
class Mobile:
    def __init__(self):
        self.model='Realme'
    def show_model(self):
        self.model

realme=Mobile()
print(realme.model)


#Accessing class variables inside class
class Mobile:
    fp="yes"
    def __init__(self):
        self.model="Realme X"
    def show_model(self):
        print(self.model)

    @classmethod
    def is_fp(cls):
        print(cls.fp)

realme=Mobile()
realme.is_fp()

#Accesing class variable outside class
class Mobile:
    fp="Yes"

@classmethod
def show(cls):
    cls.fp

print(Mobile.fp) #We can accesss class variable using classname



