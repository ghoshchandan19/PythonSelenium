x=1
while x<=10:
    print(x)
    x+=1

"""Print sum of first n naturals numbers"""
n=int(input("Enter a number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print("The sum of first",n,"naturals number is",sum)