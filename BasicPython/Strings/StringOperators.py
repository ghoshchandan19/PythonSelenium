#Mathematical operator
print("durga"+"soft")
print("durga"*3)

#program to access characters in forward direction
s="Chandan"
n=len(s)
i=0
while i<n:
    print(s[i],end='')
    i+=1
print()

#program to access characters in backward direction
s="Chandan"
n=len(s)
i=n-1
while i>=0:
    print(s[i],end="")
    i-=1
print()

#program to remove duplicates characters from string
srg="Chandan Ghosh"
s=set(srg)
s="".join(s)
print("Without Order:",s)
t=""
for i in srg:
    if i in t:
        pass
    else:
        t=t+i

print("With order:",t)

#Membership operators
s="durga"
print("d" in s)

s=input("Enter a string:")
s1=input("Enter a sub string:")
if s1 in s:
    print(s1,"is found in main string")
else:
    print(s1,"is not found in main string")

#Comparision operators
l1=["A","B","C","D"]
l2=["A","B","C","D"]
print(id(l1))
print(id(l2))
print(l1 is l2)

city=input("Enter city name:")
list=["Hyderabd","Delhi","Mumbai","Bangalore"]
if city in list:
    print("Your city is present in the list")
else:
    print("Your city is not present in the list")
print()

#Counting substring in given strings
s="durgasoftdurgasoftdurgasoft"
print(s.count("soft"))
print(s.count("soft",2,15))

#replacing a string with another string
s="Learning python is difficult"
s=s.replace("difficult","easy")
print(s)

s="ababab"
s1.replace("a","b")
print(s)
print(s1)
print(id(s))
print(id(s1))

