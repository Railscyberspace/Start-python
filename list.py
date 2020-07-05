# list
slang = ['pip', 'yonk', 'cherrio']
slang.append('yonk')
print(slang)


slang = ['pip pop', 'rice', 'bean']
del slang[2]
print(slang)
# Handling error in our programimg
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid Value')

# Classes


class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()
point1.x = 10
point1.y = 30
print(point1.x)
point1.draw()


point2 = Point()
point2.x = 1
print(point2.x)


# Constructor
point2 = Point()
point2.x = 1
print(point2.x)


# with open('/path/from/where/you/want/to/read/file') as file_one, \
#       open('/path/where/you/want/the/file/to/be/written', 'w') as file_two:
#    file_two.write(file_one.read())


# class Person:
#    def __init__(self, nane):
#       self.name = name

#   def talk(self):
#       print(f'Hi, Iam {self.name}')


#John = Person('John smith')
# John.talk()


#bob = Person('Bob smith')
# bob.talk()


# To continue from here tommmorow early morning


Times = [4, 5, 6, 5, 10, 3]
max = Times[5]
for Time in Times:
    if Time > max:
        max = Time
print(Times)

