#Tuple concatenation
print((1,2,3)+(4,5,6))

#Tuple multilication
print(('repeat')*3)

t=(10,20,30,40,50,10,50)
print(len(t))
print(t.count(10))
print(t.index(10))

print(sorted(t))

#Min and max of tuple
t1=(30,10,40,50,70)
print(min(t1))
print(max(t1))

t2='durga'
print(min(t2))
print(max(t2))

#Comparing two from_tuples
t1=(10,20,30)
t2=(40,50,60)
print(t1<t2)

#Tuple packing and Unpacking
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)

t=(60,90,70,80)
a,b,c,d=t
print(a)
print(b)
print(c)
print(d)

