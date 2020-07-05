c = 5
while c != 1:
    print(c)
    c -= 1

while True:
    response = input('Responses: ')
    if int(response) % 7 == 0:
        break


Name = 'Ruby'
Child = 'Baby'
Attitude = 'less troublesome.'
my_baby = '{} {} is now {} '
print(my_baby.format(Name, Child, Attitude))
