

#Sample for object slicing 

shoplist = ['apple', 'banana', 'mango', 'orange']

print('1st element is :', shoplist[0])
print('3rd element is :', shoplist[2])

print('Elements between 1 amd 3', shoplist[1:3])
print('Elements between -1 amd 1', shoplist[-1:1])

print('Reverse list', shoplist[::-1])
print('Elements with stepping 1', shoplist[::1])
print('Elements with stepping 2', shoplist[::2])
print('Elements with stepping 3', shoplist[::3])