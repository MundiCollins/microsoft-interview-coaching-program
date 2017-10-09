import unittest

def encrypt(string):
	key = string.split(":")[0]
	characters = string.split(":")[1]

	cipher = ''

	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	uppercase = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	# no shift
	if key == '0':
		return characters

	for i in range(len(characters)):
		if 'a' <= characters[i] <= 'z':
			# negative indexes to allow circular movement
			location = lowercase.index(characters[i]) - len(lowercase)
			cipher += lowercase[location+int(key)]
		elif 'A' <= characters[i] <= 'Z':
			location = uppercase.index(characters[i]) - len(uppercase)
			cipher += uppercase[location+int(key)]
		elif '0' <= characters[i] <= '9':
			location = digits.index(characters[i]) - len(digits)
			cipher += digits[location+int(key)]
		else:
			cipher += characters[i]

	return cipher

class Test(unittest.TestCase):
	# Test Cases
    
    data = [('2:h5lLo', 'j7nNq'), ('3:Ab&c*', 'De&f*')]
    def test_encrypt(self):
		for [test_string, expected] in self.data:
			actual = encrypt(test_string)
			self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()