import unittest

def encrypt(string):
	key = string.split(":")[0]
	key = int(key)
	characters = string.split(":")[1]

	cipher = ''

	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	# no shift
	if key == 0:
		return characters

	elif key > 0:
		for i in range(len(characters)):
			if 'a' <= characters[i] <= 'z':
				key = key % 26
				location = lowercase.index(characters[i]) - 26
				cipher += lowercase[location+key]
			elif 'A' <= characters[i] <= 'Z':
				key = key % 26
				location = uppercase.index(characters[i]) - 26
				cipher += uppercase[location+key]
			elif '0' <= characters[i] <= '9':
				key = key % 10
				location = digits.index(characters[i]) - 10
				cipher += digits[location+key]
			else:
				cipher += characters[i]

	else:
		for i in range(len(characters)):
			if 'a' <= characters[i] <= 'z':
				key = - (abs(key) % 26)
				location = lowercase.index(characters[i]) - 26
				cipher += lowercase[location+key]
			elif 'A' <= characters[i] <= 'Z':
				key = - (abs(key) % 26)
				location = uppercase.index(characters[i]) - 26
				cipher += uppercase[location+key]
			elif '0' <= characters[i] <= '9':
				key = - (abs(key) % 10)
				location = digits.index(characters[i]) - 10
				cipher += digits[location+key]
			else:
				cipher += characters[i]

	return cipher


class Test(unittest.TestCase):
	# Test Cases   
    data = [('2:h5lLo', 'j7nNq'), ('3:Ab&c*', 'De&f*'), ('-52000000:azb', 'azb'), ('104000:73C#', '73C#'), ('-20000:19', '19'), ('-27:z', 'y')]
    def test_encrypt(self):
		for [test_string, expected] in self.data:
			actual = encrypt(test_string)
			self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()