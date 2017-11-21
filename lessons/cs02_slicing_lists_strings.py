def main():
	"""
	Slicing Lists and Strings

	my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	Index:     0, 1, 2, 3, 4, 5, 6, 7, 8, 9
	Index:   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

	list[start:end:step]

	1). Prints url
	2). Prints url reversed
	3). Prints top level domain
	4). Prints url without the http://
	5). Prints url without the http:// or the top level domain
	"""
	sample_url = 'http://coreyms.com'

	print(sample_url)
	print(sample_url[::-1])
	print(sample_url[-4:])
	print(sample_url[7:])
	print(sample_url[7:-4])


if __name__ == '__main__':
	main()
