def insertionSort(array):
	"""Sorting algorithm that compares each element and orders inplace

	Time Complexity: O(n²), Ω(n)
	Space Complexity: O(1)
	"""

	for j in range(1, len(array)):
		key = array[j]
		i = j - 1
		while i >= 0 and array[i] > key:
			array[i + 1] = array[i]
			i = i - 1
		array[i + 1] = key

def main():
	a = [1, 4, 0, -3, 2, 7]
	insertionSort(a)
	print(a)


if __name__ == '__main__':
    main()