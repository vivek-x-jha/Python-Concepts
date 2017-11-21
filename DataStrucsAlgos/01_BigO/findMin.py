from tools.utility import logtimer


def main():
	"""
	Finds the minimum number in a list
	findMin1:  O(n^2)
	findMin2:  O(n)
	"""
	n = 3

	findMin1(range(10 ** n))
	findMin1(range(10 ** (n + 1)))
	findMin2(range(10 ** n))
	findMin2(range(10 ** (n + 1)))


@logtimer
def findMin1(array):
	"""Finds min number in a list in O(n^2) time"""
	for i in range(len(array)):
		min_val = array[i]
		for num in array:
			if num < min_val:
				min_val = num
	return min_val


@logtimer
def findMin2(array):
	"""Finds min number in a list in O(n) time"""
	min_val = array[0]
	for num in array:
		if num < min_val:
			min_val = num
	return min_val


if __name__ == '__main__':
	main()
