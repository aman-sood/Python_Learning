
def isPalindrome(text):
	return text == text[::-1]

sentence = input('Eneter a string to test :')
if isPalindrome(sentence):
	print('Yes, string is palindrome')
else :
	print('No, string is palindrome')