t=()#empty tuple
t=(10,0)#single element tuple
t=(10,20,30)#multiple element tupl

#Accessing element from tuple
tuple=('p','q','e','r')
print(tuple[0])
print(tuple[1])
print(tuple[3])
print(tuple[2])

#Accessing using slicing
t=('p','q','r','s','t')
print(t[1:4])
print(t[4:])
print(t[:])

#Nested tuple
nested_tuple=('mouse',[8,9,1],(1,2,3))
print(nested_tuple[0][2])
print(nested_tuple[1])
print(nested_tuple[2][2])
