# Python program to find the factorial of a number provided by the user.

# change the value for a different result
import time
num = 7

# uncomment to take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)


# Lists


# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
print("List containing multiple values: ")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)

# Program to demonstrate
# space-time trade-off between
# dictionary and list
# To calculate the time
# differenc
# Creating a dictionary

d = {'john': 1, 'alex': 2}

x = time.time()

# Accessing elements
print("Accessing dictionary elements:")
for key in d:
    print(d[key], end=" ")

y = time.time()
print("\nTime taken by dictionary:", y-x)

# Creating a List
c = [1, 2]

x = time.time()

print("\nAccessing List elements:")
for i in c:
    print(i, end=" ")

y = time.time()
print("\nTime taken by dictionary:", y - x)

