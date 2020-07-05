# guess game(while loop)
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('You loose!')


# Car Game (While loop)
command = ""
started = False
stop = False
while True:
    command = input('>').lower()
    if command == 'start':
        print('car started')
        if started:
            print('car already started!')
        else:
            started = True
    elif command == 'stop':
        print('car has stopped')
        if not started:
            print('Car has already stopped!')
        else:
            started = False
    elif command == 'help':
        print('''
start--- To start the car)
stop - ---To stop the car
quit ----help''')
    elif command == 'quit':
        break
    else:
        print('I do not understand that')


# for loop
for item in ['sunday', 'Abam', 'john']:
    print(item)

for item in range(10):
    print(item)


# loop range
prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
    print(f'total:{total}')

# Nested Loop
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

number = [5, 2, 3, 5, 2]
for x_count in number:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# List
names = ['John', 'Smith', 'Sunday', 'Abam']
print(names[:-1])


# Looking for the largest number in a list
numbers = [3, 5, 7, 2, 15]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
matrix[1][2] = 20
print(matrix[1][2])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for row in matrix:
    for item in row:
        print(item)
else:
    print(matrix)

# Methods in list idex,pop to delete last element in the list,clear to delete all element,insert to add element,apphend to add element together
numbers = [5, 2, 1, 4, 8]
numbers.append(20)
print(numbers)


numbers = [5, 2, 1, 4, 8]
numbers.insert(1, 15)
print(numbers)


numbers = [5, 5, 2, 2, 1, 4, 8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


# Tuple
numbers = (5, 2, 1, 4, 8)
numbers.index(2)
print(numbers)


coordinates = [1, 2, 3]
x, y, z = coordinates
print(f'{x},{y},{z}')


# Dictionary. we use this to get users details.
costomer = {
    'name': 'John smith',
    'age': 27,
    'Email': 'abamsunday5@gmail.com'
}
print(costomer.get('birthday'))


Phone = input('Phone: ')
digits_mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
}
output = ''
for ch in Phone:
    output += digits_mapping.get(ch, "!") + ''   ''
print(output)


# Emoji converter
message = input('>')
words = message.split('   ')
emoji = {
    ':)':  '😙',
    ': (':  '😆'
}
output = ''
for word in words:
    output += emoji.get(word, word) + '' ''
print(output)


def emoji_converter(message):
    word = message.split('  ')
    emojis = {
        ':)': '😆',
        ':(':  '🌝'
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input('>')
print(emoji_converter(message))


# LIST
greetings = ['cherrs', 'Hello', 'cheerio']
print(greetings[3])
