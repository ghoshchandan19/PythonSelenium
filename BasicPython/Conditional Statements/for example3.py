""" program to print from 100 to 1"""
for x in range(100,0,-1):
    print(x)

"""program to print sum of list"""
list=eval(input("enter some value in list"))
sum=0
for x in list:
    sum=sum+x
print(sum)

"""Print stars pattern"""

n=int(input("Enter number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

