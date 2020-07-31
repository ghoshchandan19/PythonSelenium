s1={10,20,50,78}
s2={65,78,87,87}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.symmetric_difference_update(s2))

s1=set('durga')
print(s1)
print('d' in s1)
print('z' in s1)

#Set comprehensions
s={x*x for x in range (1,6)}
print(s)

s2={78,98,18,87,77}
print(sum(s2))
print(max(s2))
print(min(s2))

#Iterating through a set
s={'a','e','i','o','u'}
for l in s:
    print(l)