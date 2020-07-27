# A list inside a list is called nested list
x=[10,20,[30,40]]
print(x)
print(x[1])
print(x[2])
print(x[2][1])

#print nested list in matrix structure
x=[[10,20,30],[40,50,60],[70,80,90]]
print(x)
for r in x:
    print(r)

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=' ')
print()