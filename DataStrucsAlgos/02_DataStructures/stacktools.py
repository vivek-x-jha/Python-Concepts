from concepts.DataStrucsAlgos.pythonds import Stack


def revstring(mystr):
	"""Reverse given string using a stack"""
	s = Stack()
	for char in mystr:
		s.push(char)

	revstr = ''
	while not s.isEmpty():
		revstr += s.pop()

	return revstr


def parchecker(symbolString):
	pass


def main():
	assert revstring('apple') == 'elppa'
	assert revstring('x') == 'x'
	assert revstring('1234567890') == '0987654321'
	# assert parChecker('((()))')
	# assert not parChecker('(()')


if __name__ == '__main__':
	main()
