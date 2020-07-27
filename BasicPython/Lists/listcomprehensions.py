list=[]
for x in range(1,11):
    list.append(x*x)
print(list)

list=[x for x in range(1,21) if x%2==0]
print(list)#even numbers from 1 to 21

words=['Balaih','Nag','Venkatesh','Chitu']
l=[w[0] for w in words]
print(l)

l=[w for w in words if len(w)>6]
print(l)

n1=[10,20,30,40]
n2=[30,40,50,60]
n3=[x for x in n1 if x not in n2]
print(n3)

words="the quick brown fox jumps over the lazy dog".split()
print(words)
l=[w.upper() for w in words]
print(l)

