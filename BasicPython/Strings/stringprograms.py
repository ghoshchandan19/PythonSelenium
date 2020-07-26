"""
program to seperate alphabets and numbers from
input=B4A57C6F
OUTPUT=ABCF5467
"""
s=input("Enter a aplhanumeric string")
s1=s2=output=""
for x in s:
    if x .isalpha():
        s1=s1+x
    else:
        s2=s2+x
print(s1)
print(s2)
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)

"""

INPUT:a7b4c3
output:aaaaaaabbbbccc

"""
s=input("Enter a string:-")
output=""
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        print((int(x)-1))
        output=output+previous*(int(x)-1)
print(output)


