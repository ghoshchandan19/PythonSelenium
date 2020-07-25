s="Chandan Ghosh is  a good person"
print(s.split())# output will be list of stringsplit
l=s.split()
for x in l:
    print(x)

s="02-03-2028"
l=s.split('-')
print(l)
for x in l:
    print("x")


s='durga software solutions hyderabad india'
l=s.split(" ",3)
print(l)

#split from reverse direction
s="durga software solutions hyderabad india"
l=s.rsplit(" ",3)
for x in l:
    print(x)

#join string with parameters
l=['durga','software','solutions']
s='-'.join(l)
print(s)

t=('durga','soft','solutions')
s=':'.join(t)
print(s)
