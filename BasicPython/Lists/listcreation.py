from itertools import count

l=[] #empty strings
print(l)
l=[2,7,9,7,5,43]
print(len(l))
print(l)
"""
l=eval(input("Enter some list:"))# list from keyboard
print(l)
"""

s="Chandan Ghosh is a good man"
l=s.split(" ")
print(l)

#Travesring a list
list=[56,89,90,86,54,45]
i=0
while i<len(list):
    print(list[i])
    i=i+1
print()

# using for loop
for x in list:
    print(x)

list1=["A","B","C","D"]
x=len(list1)
for i in range(x):
    print(list1[i],"is availaible at positive index:", i,"and negative index:",i-x)


str=["A","B","C","D","E","F","G","H","I","J","K","A","D"]
print(len(str))
print(str.count("A"))
print(str.index("A"))
