#program to find sum of the keys in dictionary
d={101:'durga',102:'ravi',103:'siva'}
s=sum(d.keys())
print("The sum is",s)

#print numnber of occurences of each letter present in the string
word=input("Enter a word:-")
d={}
for x in word:
   d[x]= d.get(x,0)+1
print(d)
print()

#print numnber of occurences of vowels present in the string
word=input("Enter a word:-")
vowels={'a','e','i','o','u'}
count={}.fromkeys(vowels,0)

for x in word:
    if x in count.keys():
        count[x]=count[x]+1

print("number of occurencess of vowels ",count)
sum=0
for i in count.values():
    sum=sum+i
print("Total number of vowels un the string ",sum)

