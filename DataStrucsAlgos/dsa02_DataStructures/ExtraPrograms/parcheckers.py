from concepts.DataStrucsAlgos.pythonds import Stack


def main():
	assert parChecker('((()))')
	assert not parChecker('(()')

	assert symbolChecker('{{([][])}()}')
	assert not symbolChecker('[{()]')


def parChecker(symbol_str):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol_str) and balanced:
		symbol_str = symbol_str[index]
		if symbol_str == "(":
			s.push(symbol_str)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()

		index += 1

	if balanced and s.isEmpty():
		return True
	else:
		return False


def symbolChecker(symbol_str):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbol_str) and balanced:
		symbol = symbol_str[index]
		if symbol in "([{":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False
		index += 1
	if balanced and s.isEmpty():
		return True
	else:
		return False


def matches(open, close):
	opens = "([{"
	closers = ")]}"
	return opens.index(open) == closers.index(close)


if __name__ == '__main__':
	main()
