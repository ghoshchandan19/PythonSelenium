import weakref


class Car:
    def __init__(self,w):
        self.wheels=w

c1=Car(4)
print("c1 memory location:",hex(id(c1)))
r=weakref.ref(c1)
print("before :",r)
c1=None
print("After :",r)
print("Garbage Collected immediately")