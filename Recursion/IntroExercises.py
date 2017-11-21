# https://www.python-course.eu/python3_recursive_functions.php

def mult3(n):
	"""Recursive function that returns multiple of 3"""
	if n == 0:
		result = 0
	else:
		result = 3 + mult3(n - 1)

	return result


def sumOfN(n):
	"""Recursive function that returns sum of first n integers"""
	if n == 0:
		result = 0
	else:
		result = n + sumOfN(n - 1)

	return result

def pascalTriangle(n):
	if n == 1:
		result = [1]
	else:
		pass


def main():
	print([mult3(n) for n in range(10)])
	print([sumOfN(n) for n in range(10)])


if __name__ == '__main__':
	main()
