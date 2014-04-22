

# Taken from Byte of Python

age = 20
name = 'Ravi'

value = 1.0/3

print('''{0}'s age is {1}'''.format(name, age))
print('''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."''')

print('''{}'s age is {}'''.format(name, age)) # numeber are not compulsory

print('{0:.3}'.format(value))
print('{0:.3}'.format(1.0/3))
print('{0:_^15}'.format('Aman'))
print('{name1} is learning {lang}'.format(name1 = 'Aman', lang = 'Python'))

# To remove new line from print satatement in python 3.x
# print('Aman', end='')
# print('Sood', end='')

# escape sequence
print('This is the first sentence. \
This is the second sentence.')