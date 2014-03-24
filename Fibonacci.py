
def fibonacci(len):
	transitNumber = 0
	number = 1
	print(number)

	while len - 1 > 0:
		sum = transitNumber + number
		print(sum)
		transitNumber = number
		number = sum
		len = len - 1


print('--------Fibonacci Series sample-------')

len = input('Enter number of elements in series :')
while len == 0:
	print("Number of elements can't be zero")
	len = input('Please reenter :')

fibonacci(len)