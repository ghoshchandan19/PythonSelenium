s={}#Treated as empty dictionary
s=set() #Traeted as empty set
s1={10,78,90,56,89}
print(s1)
list=[90,10,89,10,67]
print(set(list))
print(set('Chandan'))

#Adding element to the list
s={10,20,30}
s.add(40)
print(s)

#Updating an set
s={10,20,30,30,40}
l=[67,89,90]
s.update(l)
print(s)

#Copying an element
s={10,20,30}
s1=s.copy()
print(s1)

#Removing elements from set
s={78,90,87,89,67}
print(s.pop())
print(s.pop())
print(s.pop())

#Removing a specific elements
s={10,70,56,78,98}
s.remove(70)
print(s)
s.remove(11) #will give key errors
print(s)

#Discard in set
s={10,70,56,78,98}
print(s.discard(70))
print(s.discard(9999))

#Clearing all the elements from set
s={10,70,56,78,98}
print(s.clear())