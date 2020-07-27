x=['Dog','Cat','Rat']
y=['Dog','Cat','Rat']
z=['DOG','CAT','RAT']
#Check the content between the two list
print(x==y)
print(x==z)
print(x!=z)

print(x is y)

a=[50,67,98,1]
b=[20,78,97,1,56]
print(x>y) #returns boolen if element present inside the list[0] and list2[0]
print(x>=y)
print(1 in a)#returns boolen if element present inside the list
print(100 in b)#returns boolen if element present inside the list

#to remove all the elements from the list
x=[10,29,29,80]
print(x)
x.clear()
print(x)