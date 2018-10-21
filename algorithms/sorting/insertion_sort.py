def insertionSort(array):
	"""Sorting algorithm that compares each element and orders inplace

	Time Complexity: O(n²), Ω(n)
	Space Complexity: O(1)
	"""

	for j in range(1, len(array)):
		key = array[j]
		i = j - 1
		while i > 1 and array[i] > key:
			pass


def main():
	a = [1, 4, 0, -3, 2, 7]
	insertionSort(a)
	print(a)


if __name__ == '__main__':
    main()