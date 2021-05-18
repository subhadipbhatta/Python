## measure the length of the list items in a function#############

def name(lst1):
    x = 0
    y = 0
    print(lst1)
    for i in lst1:
        if len(i) > 5:
            x += 1
        else:
            y += 1

    print("Number of names with more than 5 characters are {} and less than 5 characters are {}".format(x, y))


lst = []
n = int(input("Enter the number of names you want to enter   "))

for i in range(0, n):
    ele = input("Enter the name   ")
    lst.append(ele)
name(lst)


### Fibonacci using user input #####
def fib(n):
    a = 0
    b = 1
    c = 0
    print(a)
    print(b)
    while c < n - 1:
        c = a + b
        a = b
        b = c
        if c < n:
            print(c)
        else:
            break


n1 = int(input("Enter the range for fibonacci ==>> "))
fib(n1)


############# Factorial ###############
def factorial(n):
    j = 1
    if n > 1:
        for i in range(1, n + 1):
            j = j * i
    else:
        print("Enter a positive number")
    print("The factorial of ", n, "is ", j)


num = int(input("Enter a number ::: "))
factorial(num)


############# Factorial using recursion #############

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)

###### Lambda ######
from functools import reduce

nums = [2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(lambda a: a % 2 == 0, nums))
double = list(map(lambda a: a * 2, evens))
sum = reduce(lambda a, b: a + b, double)
print(evens)
print(double)
print(sum)
