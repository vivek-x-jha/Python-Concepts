# Generators in Python
#
# Source: https://wiki.python.org/moin/Generators

"""
Custom Generator Functions:
- allow you to declare a function that behaves like an iterator
- generates values "on the fly" by yielding them
- after last item is yielded, returns empty sequence
- can be used in a for loop
- range in Python 3.x is commonly used to return a generator obj when looping

Improved Performance:
- provides performance benefits only if we do not intend to use that set of generated values more than once
- performance improvement from generating values lazily (on demand) -> translates to lower memory usage
- do not need to wait until all the elements have been generated before we start to use them
- this is similar to the benefits provided by iterators, but the generator makes building iterators easy

Generator Expressions (more useful):
- provide an additional shortcut to build generators out of expressions similar to that of list comprehensions
- replace the square brackets ("[ ... ]") with parantheses ("( ... )")
- alternatively, list comprehensions are just syntatic sugar for a generator expression wrapped in a list constructor
- by allowing generator expressions, we don't have to write a generator function if we do not need the list
- if only list comprehensions were available, and we needed to lazily build a set of items to be processed, we will have to write a generator function
"""

def squareGenerator(k):
	num = 1
	while num < k:
		yield num ** 2
		num += 1


n = 10 ** 1

# Non-Pythonic design pattern
squareList = []
for num in range(1, n + 1):
	squareList.append(num ** 2)

# Generator expressions (fast, elegant, & readable) 
generatorExp = (num ** 2 for num in range(1, n + 1))

# We can even pass in generator expressions into lambda funcs
powerGeneratorExp = lambda k: (num ** k for num in range(1, n + 1))
squareGeneratorExp = powerGeneratorExp(2)
cubeGeneratorExp = powerGeneratorExp(3)

# TFAE (The following are equivalent)
squareListComp1 = list((num ** 2 for num in range(1, n + 1)))
squareListComp2 = list(num ** 2 for num in range(1, n + 1))
squareListComp3 = [num ** 2 for num in range(1, n + 1)]


def main():
	print(squareGenerator(n + 1))

	for square in squareGenerator(n + 1):
		print(square)

	print(squareList)

	for listcomp in [squareListComp1, squareListComp2, squareListComp3]:
		print(listcomp)

	assert sum(squareGeneratorExp) == n * (n + 1) * (2 * n + 1) / 6
	assert min(cubeGeneratorExp) == 1
	assert max(powerGeneratorExp(4)) == n ** 4

if __name__ == '__main__':
	main()
