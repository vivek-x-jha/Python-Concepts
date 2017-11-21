from tools.utility import logtimer


def main():
	n = 7

	list_concat(10 ** n)
	list_concat(10 ** (n + 1))
	list_append(10 ** n)
	list_append(10 ** (n + 1))
	list_comp(10 ** n)
	list_comp(10 ** (n + 1))
	list_range(10 ** n)
	list_range(10 ** (n + 1))


@logtimer
def list_concat(n):
	"""
	Concatenating
	O(k), k = list size being concatenated
	"""
	alist = []
	for i in range(n):
		alist += [i]

	# return alist


@logtimer
def list_append(n):
	"""
	Append Method
	O(1)
	"""
	alist = []
	for i in range(n):
		alist.append(i)

	# return alist


@logtimer
def list_comp(n):
	"""
	List Comprehension
	O()
	"""
	alist = [i for i in range(n)]

	# return alist


@logtimer
def list_range(n):
	"""
	List Comprehension
	O()
	"""
	alist = list(range(n))

	# return alist


if __name__ == '__main__':
	main()
