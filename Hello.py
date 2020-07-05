
import math
if 5 > 2:
    print('Five is greater than two! ')
else:
    print('two is greater than five')


# v Variable Names.
name = 'vivcis'
age = 27
print(name)
print(age)

# legal variable names
myvar = 'John'
my_var = 'John'
_my_var = 'John'
myVar = 'john'
MYVAR = 'John'
myvar2 = 'John'

# illegal variable names
# 2myvar = 'John'
# my-var = 'John'
# my var = 'John'


first_name = 27
first_name = 'sally'
print(first_name)


# Assigning values to multiple variables.
shoplist, market, farm = 'meat', 'plantain', 'rice'
print(shoplist)
print(market)
print(farm)

name = 'Sunday'
print('Hello ' + name)


# Output Variables.
first_name = 'Sunday'
last_name = 'Abam'
total = first_name + last_name
print(total)

# if you try to combine a number and a string python will give you typeError.but string to string,Num to num welcome.
first = 10
second = 12
print(first + second)

# Global Variables
# Global variable can be used inside of function and outside.


# Global Keyword
# Python Data Types.
# Build In By default

# str:(text type)
# int:(int,float,complex)
# list,tuple,range:(sequence typees)
# dict:(mapping type)
# set,frozenset:(set types)
# bool:(boolean type)
# bytearray,memeoryview:(binary types)

age = 27  # number
first_name = False  # bool
last_name = 'Sunaday'  # string
print(type(last_name))
print(type(first_name))
print(type(age))

num = 20.7
print(type(num))  # float

letter = 1j
print(type(1j))  # complex

let = ['apple', 'banna']
print(type(let))  # list

time = range(6)
print(type(time))  # range

x = b"Hello"
print(type(x))  # bytes

# Python Numbers.
# numeric types in python
# int, float, complex

# specifying  a variable Type
int()
float()
str()
python = int(2.3)
print(python)  # output (2)

float()
num = float(1)
print(num)  # output (1.0)

xy = float(4.5)  # Output(4.5)
print(xy)

str()
hour = str("30")  # Output (30)

str()
num = str(5.8)  # Output (5.8)
print(num)

# Python String
freedom = '''
All things are lawful,
but not all things are advantageous
. All things are lawful,
 but not all things build up.
 '''
print(freedom)

# String are Arrarys
# Output is (t) python minus the first letter and start from the second.
freedom = 'advantageous'
print(freedom[5])
# slicing
freedom = 'advan,tageous'
# Output(van) python will stand counting from the v which is the three letter but fall in index (2)
print(freedom[2:5])

thing = ' lawful'
# Output(awf) python will start from a because thefirst letter start from index (0).
print(thing[2:5])

# Negative indexing
freedom = 'Hello,world'
# Output is (wor) python count from left to were the index 5 is and count and again from right to were index 2 is
print(freedom[-5:-2])

# String Length
hour = 'Hello, world'
print(len(hour))  # Output (12) python added 1 on both side

# string Methods(strip)
hour = 'Hello, world'
print(hour.strip())  # output(Hello, World)

# upper
hour = 'Hello, World'
print(hour.upper())

# lower
hour = 'HELLO,WORLD'
print(hour.lower())

# replace
hour = 'thanks, you'
print(hour.replace('h', 'j'))  # output(tjanks,you)

# split()
time = 'Hello,World'
print(time.split(','))

longtime = 'how are you,hope you are doing well?'
print(longtime.split(','))

# Checking String.
text = 'it rain heavy rain in spain'
msg = 'ain' in text
print(msg)  # output is (true)


text = 'it rain heavy rain in spain'
msg = 'ain' not in text
print(msg)  # output is (False)

# string concantenation
let = 'Hello'
const = 'World'
total = let + const  # output (Helloworld)
print(total)

let = 'Hello'  # putting space in between the strings.
const = 'World'
total = let + '  ' + const  # output (Hello world)
print(total)

# string formating
# Age = 27
# text = 'My name is vivcis, i am' + Age #out error message (can not contenate str and number)
# print(text)

Age = 27
text = 'My name is vivcis, i am {}'
print(text.format(Age))


quantity = 27
item_numbber = 205
price = 57.23
my_Order = 'i want to buy {} of {} worth {} dollars'
print(my_Order.format(quantity, item_numbber, price))


quantity = 27
item_numbber = 205
price = 57.23
my_Order = 'i want to pay {2} dollar for {0} pieces '
print(my_Order.format(quantity, item_numbber, price))

Email = '''
 Hi, Vivcis
   This is my first email ,
   to you,
Thank you for been a start.Ng friend   🙂
'''
print(Email)

let = 1  # int()
const = 24.5  # float
var = 45j  # complex
# converting from int to float.
time = float(1)  # output (1.0)float
print(time)

# converting from float to int
Hour = int(24.5)  # output is (24)int
print(Hour)

# converting from int to complex
Time = complex(1)
print(Time)

course = 'python for programming'
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])


course = 'python \'programming'
print(course)

course = 'python \nprogramming'
print(course)


First = 'Sunday'
Last = 'Abam'
full_Name = First + ' ' + Last
print(full_Name)

# formating method
First = 'Sunday'
Last = 'Abam'
full_Name = f'{len(First)} {Last}'
print(full_Name)

course = 'python for programming'
print(course.find('pyt'))
print(course.strip())
print(course.lower())
print(course.title())
print(course.replace('p', 'j'))
print('switch' not in course)


print(10 + 3)
print(20 - 3)
print(10 * 3)
print(20 / 3)
print(20 // 3)
print(20 ** 3)
print(20 % 3)


x = +3
print(x)

# import math
print(round(3.9))
print(abs(-3.7))

print(math.ceil(3.5))

x = input('x: ')
y = int(x) + 1
print(f'x: {x}, y: {y}')

temperature = 15
if temperature > 30:
    print('it wram weather')
    print('drink water')
elif temperature > 20:
    print('it nice')
else:
    print('it cold')
print('done')

10 > 3
ord('b')

temperature = 30
if temperature > 30:
    print('it warm')
    print('drink water')
elif temperature > 20:
    print('it nice')
else:
    print('it cold')
print('done')

# if(password > 5):
# print('please it a valid password')
# else:
# print('invalid password')

# if statement
age = 12
message = 'Eligible' if age >= 18 else 'Not Eligible'
print(message)

# loops (and)
high_income = False
good_credit = True

if high_income and good_credit:
    print('Eligible')
else:
    print('Not Eligible')


high_income = True
good_credit = False
message = 'Eligible' if high_income and good_credit else 'Not Eligible'
print(message)


high_income = True
good_credit = False
message = 'Eligible' if high_income or good_credit else 'Not Eligible'
print(message)

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print('Eligible')
else:
    print('Not Eligible')

# Age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print('Good to go')
else:
    print('Not good to go')

# loops
for number in range(1, 4):
    print('This email is from us', number, number * '.')


# Ending a sucessful messgsge first attempt.
sucessful = True
if number in range(3):
    print('This is email is from us')
    if sucessful:
        print('sucessful')
else:
    print('attempted three times and fails')

good_credit = False
good_income = True
student = True
if good_credit or good_income and not student:
    print('Eligible')
else:
    print('Not Eligible 😙')
# Nested loops
for x in range(5):
    for y in range(3):
        print(f'({x}, {y})')

# lteration
for x in "Python":
    for y in "language":
        print(f'({x},{y})')

for x in [1, 2, 3, 4]:
    print(x)

   # command = ''
    # while command.lower() != 'quite':
    #  command = input('>')
    # ('ECHO', command)

while True:
    command = input('>')
    print('ECHO', command)
    if command.lower() == 'quit':
        break


number = 100
while number > 0:
    print(number)
    number //= 2

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'we have {count} even numbers')

# Functions


def function(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome aboard')


function('Sunday', 'Abam')


# Input
First_name = input('First_Name: ')
Last_Name = input('Last_Name: ')
Gender = input('Gender: ')
Status = input('Status: ')
Phone = input('Phone: ')


def Hello(name):  # parameters
    print(f'Hi {name}')


Hello('Sunday')  # Agrument


def greet(name):
    print(f'wow {name}')


def get_greeting(name):
    return f'wow {name}'


message = get_greeting('Sunday')
file = open('content.txt', 'w')
file.write(message)


# Keyword Aruguments
def increment(number, by):  # or we can write it this way (number , by =1)
    return number + by


print(increment(2, by=1))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total


print('Start')
print(multiply(2, 3, 4, 6))


def save_user(**user):
    print(user)

    save_user(id=1, name='Sunday', age=26)


command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        print("car started....")
    if started:
        print("car has already started")

        print('''
start--to start the car)
stop - -to stop the car
quit - -to quit
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry we don't understand you")


first_Name = "John"

if len(first_Name) < 4:
    print('Name must be at least 3 charaters')
elif len(first_Name) > 50:
    print('Name must be a maxmium of 15 characters')
else:
    print("Name looks good")


Email = input('Email: ')
if len(Email) > 7:
    regex = '@+[?][q-zA-Z0-9-.] &', Email != None
    print('This is  a valid Email 🙂')
else:
    print('Invalid Email')

weight = int(input('weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')

