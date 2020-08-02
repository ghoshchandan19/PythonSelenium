d={}
d[100]='durga'
d[101]='chandan'
print(d)
#To retrieve values from the key
print(d[100])
print(d[101])
print(101 in d)

#updating dictionary
d={101:'durga',102:'ravi',103:'siva'}
d[101]='chandan'
print(d)

#deleting dictionary
d={101:'durga',102:'ravi',103:'siva'}
del d[101]
print(d)
d.clear()
print(d)

#insert multiple values in the same key
list=["Hyderabd","chennai","delhi"]
d={101:list}
print(d)

#prints the length of the dictionary
print(len(d))

#To get the values of the keys
d={101:'durga',102:'ravi',103:'siva'}
print(d.keys())

#To remove the key value & return
d={101:'durga',102:'ravi',103:'siva'}
print(d.popitem())

#To retrieve keys
d=dict({100:'chandan',101:'ravi'})
print(d.keys())
for k in d.keys():
    print(k)

#Cloning a dictionary
d=dict({100:'chandan',101:'ravi'})
d1=d.copy()
print(d1)

#Updating a dictionary
d={101:'durga',102:'ravi',103:'siva'}
d1={'a':'apple','b':'guava'}
d.update(d1)
print(d)

#dictionary comprehension


