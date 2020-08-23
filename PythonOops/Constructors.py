#Cosntructor without parameters
class Mobile:
    def __init__(self):
        self.model ='RealMe X'

    def show_model(self):  # Method to call the instance variable
        print('Model', self.model)

realme=Mobile()
realme.show_model()

#Constructor with parameters
class Mobile:
    def __init__(self,m):
        self.model =m
    def show_model(self):
        print('Model', self.model)

realme=Mobile("RealMe X")
realme.show_model()
