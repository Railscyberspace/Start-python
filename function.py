def emoji_converter(message):
    word = message.split('  ')
    emojis = {
        ':)': '😆',
        ':(':  '🌝'
    }
    output = ''
    for word in word:
        output += emojis.get(word, word) + ' '
    return output


message = input('>')
print(emoji_converter(message))


# exceptions
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age can not be 0')
except ValueError:
    print('Invalid value')

# Classes


class Person:
    def __init__(self, nane):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


John = Person('John smith')
John.talk()


bob = Person('Bob smith')
bob.talk()

# inheritance


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass

    class Cat(Mammal):
        def be_annoying(self):
            print("annoying")


dog1 = Dog()
dog1.walk()


# Modules
