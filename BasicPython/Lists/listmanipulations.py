# Adding in the list
l=[]
l.append(10)
l.append(20)
l.append(30)
print(l)

l=[]
for x in range(101):
    if x%2==0:
        l.append(x)
print(l)

#insert in the list1
l=[]
l.append(10)
l.append(20)
l.append(30)
print(l)
l.insert(1,50)
print(l)
l.insert(50,777)
print(l)
l.insert(-10,9999)
print(l)
print(l.index(777))
print(l.index(9999))

#Adding one list to other list
l1=["Chicken","Mutton","Fish"]
l2=["kfc","RC","fo"]
l1.extend(l2)
print(l1)
print(l2)

#reversing a list in ascending order
l=[20,0,9,56,77]
l.sort(reverse=False)
print(l)