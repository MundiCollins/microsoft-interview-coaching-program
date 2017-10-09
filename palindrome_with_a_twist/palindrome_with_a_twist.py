import unittest

def isPalindrome(number):

	try:
		number = int(number)

		reverse = str(number)[::-1]

		if number == int(reverse):
			return str(number) + " is a palindrome"

		while(number <= 1000000):

			if check(number):
				return "Found palindrome: " + str(number)

			reverse = str(number)[::-1]
			number += int(reverse)

		return False

	except ValueError:
		return "Invalid input"

def check(number):
	reverse = str(number)[::-1]

	if number == int(reverse):
		return True

	return False


class Test(unittest.TestCase):
	dataOriginalPalindromes = [1, 22, 121, 555, 3663, 100103]
	dataGeneratedPalindromes = [12, 13, 19, 100103]
	dataInvalidInput = ['%', 'asdf', '12e', '5/', -56]

	def testPalindrome(self):
		for test_number in self.dataOriginalPalindromes:
			print(isPalindrome(test_number))		

		for test_number in self.dataGeneratedPalindromes:
			print(isPalindrome(test_number))

		for test_number in self.dataInvalidInput:
			print(isPalindrome(test_number))

if __name__ == "__main__":
	unittest.main()
