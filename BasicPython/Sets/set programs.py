#eliminate duplicates from the list
list=eval(input("enter some values:-"))
s=set(list)
print(s)
print()

#find different vowels in Words
w=input("Enter word:-")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print(d)