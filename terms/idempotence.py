"""
Programming Terms: Idempotence
https://youtu.be/UaKZ4wKytcA
"""


def idemp(func, arg):
	try:
		if func(arg) == func(func(arg)):
			print('{} is idempotent.'.format(str(func)))
		elif func(arg) != func(func(arg)):
			print('{} is not idempotent.'.format(func))
	except Exception as e:
		print(f'{type(e).__name__}: {repr(e)}')


if __name__ == '__main__':
	def add_ten(num):
		return num + 10


	# idempotent
	idemp(abs, 'st')
	# assert
	# not ®idempotent
	idemp(add_ten, 5)
