from tools.utility import logtimer


@logtimer
def sumN(n):
	"""Looping through: O(n)"""
	return sum(i for i in range(n + 1))


@logtimer
def sumN2(n):
	"""Closed form: O(1)"""
	return n * (n + 1) // 2


def main():

	n = 6

	sumN(10 ** n)
	sumN(10 ** (n + 1))
	sumN2(10 ** n)
	sumN2(10 ** (n + 1))


if __name__ == '__main__':
	main()
