from misc.decorators import logtimer


def main():
	assert anagramSolution1('abcd', 'dcba')
	assert anagramSolution2('abcde', 'edcba')
	assert anagramSolution4('apple', 'pleap')


def anagramSolution1(s1, s2):
	"""
	Checks if 2 given strings are anagrams of each other
	Runtime: O(n^2)
	"""
	alist = list(s2)

	i = 0
	result = True

	while i < len(s1) and result:
		j = 0
		found = False
		while j < len(alist) and not found:
			if s1[i] == alist[j]:
				found = True
			else:
				j += 1

		if found:
			alist[j] = None
		else:
			result = False

		i += 1

	return result


def anagramSolution2(s1, s2):
	"""
	Checks if 2 given strings are anagrams of each other
	Runtime: O(n log n)
	"""
	alist1 = list(s1)
	alist2 = list(s2)

	alist1.sort()
	alist2.sort()

	i = 0
	matches = True

	while i < len(s1) and matches:
		if alist1[i] == alist2[i]:
			i += 1
		else:
			matches = False

	return matches


def anagramSolution4(s1, s2):
	"""
	Checks if 2 given strings are anagrams of each other
	Runtime: O(n)

	Though this runs in linear time, the trade off is that it takes more space
	"""
	c1 = [0] * 26
	c2 = [0] * 26

	for i in range(len(s1)):
		j = ord(s1[i]) - ord('a')
		c1[j] += 1

	for i in range(len(s2)):
		j = ord(s2[i]) - ord('a')
		c2[j] += 1

	j = 0
	result = True
	while j < 26 and result:
		if c1[j] == c2[j]:
			j += 1
		else:
			result = False

	return result


if __name__ == '__main__':
	main()
