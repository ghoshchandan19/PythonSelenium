s="durga"
print(s[0])

#print all the characters from the string starting

str=input("Enter a text:")
i=0
for x in str:
    print("The characters is at positive index {} and negative index:{} is :{}".format(i,i-len(str),x))
    i+=1

#Slice operator
s="durga"
print("Length of string",len(s))
print(s[0:3:1])
print(s[0:3:2])
print(s[0:3:0])
print(s[0:7:1])

