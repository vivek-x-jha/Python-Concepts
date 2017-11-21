from tools.utility import logtimer


def main():
	n = 5
	kmin1(range(10 ** n))
	kmin1(range(10 ** (n + 1)))
	kmin2(range(10 ** n))
	kmin2(range(10 ** (n + 1)))


@logtimer
def kmin1(array, k=1):
	"""
	Finds kth smallest number, given list of numbers in random order
	Runtime:    O(n log(n))
	"""
	array.sort()
	return array[k - 1]


@logtimer
def kmin2(array, k=1):
	"""
	Finds kth smallest number, given list of numbers in random order
	Runtime:    O(n)
	"""
	pass


if __name__ == '__main__':
	main()
