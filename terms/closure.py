"""
Programming Terms: Closures - How to Use Them and Why They Are Useful
https://youtu.be/swU3c34d2NQ
"""


def closure(func):
	def wrapper(*args, **kwargs):
		print(f'This adds functionality before "{func.__name__}"')
		result = func(*args, **kwargs)
		print(f'This adds functionality after "{func.__name__}"')

		return result

	return wrapper


def add(x, y):
	return x + y


def sub(x, y):
	return x - y


add_closure = closure(add)
sub_closure = closure(sub)

if __name__ == '__main__':
	print(add_closure)
	print(sub_closure)
