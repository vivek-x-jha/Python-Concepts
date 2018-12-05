from concepts.DataStrucsAlgos.pythonds import Stack


def baseConverter(decNumber, base):
	digits = "0123456789ABCDEF"
	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % base
		remstack.push(rem)
		decNumber = decNumber // base

	newString = ""
	while not remstack.isEmpty():
		newString += digits[remstack.pop()]

	return newString


def main():
	assert baseConverter(25, 2) == '11001'
	assert baseConverter(25, 16) == '19'
	assert baseConverter(25, 8) == '31'
	assert baseConverter(256, 16) == '100'
	assert baseConverter(26, 26) == '10'


if __name__ == '__main__':
	main()
