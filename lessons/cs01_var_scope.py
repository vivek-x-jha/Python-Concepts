def main():
	"""
	Variable Scope - Understanding the LEGB rule and global/nonlocal statements
	"""
	for a in range(2):
		x = f'global {a}'


	def outer():
		# x = 'outer x'
		for b in range(3):
			x = f'outer {r}'

		def inner():
			# x = 'inner x'
			for c in range(4):
				x = f'inner {c}'
			print(x)
			print(a, b, c)

		inner()
		print(x)
		print(a, b)

	outer()
	print(x)
	print(a)


if __name__ == '__main__':
	main()
