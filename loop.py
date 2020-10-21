"""1: Print First 10 natural numbers using while loop"""

i=0

while (i<=10):
    print(i)
    i=i+1

"""2: Print the following pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")


"""Make a program that lists the countries in the set below using a while loop.

clist = ["Canada","USA","Mexico"]"""

len = 3
clist = []

while (len>0):
    country = input("enter the country name")
    clist.insert(len,country)
    len=len-1

print(clist)

"""
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""


for row in range (9):
    for col in range (row):
        print("*",end="")
    print("")

for row in range (9,0,-1):
    for col in range (row):
        print("*",end="")
    print("")


"""Write a Python program that accepts a word from the user and reverse it. """

word = input("Enter the word ==>")

for i in range(len(word)-1,-1,-1):
    print(word[i],end="")
print("\n")
