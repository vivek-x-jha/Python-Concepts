"""
Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions
https://youtu.be/FsAPt_9Bf3U
"""
from functools import wraps


def decorator(func):
	"""Decorator w/o @wraps DocString"""

	def wrapper(*args, **kwargs):
		"""Wrapper w/o @wraps DocString (This should not be appearing)"""
		print('Wrapper Running: \tw/o @wraps')
		return func(*args, **kwargs)

	return wrapper


def decorator_wraps(func):
	"""Decorator w/ @wraps DocString"""

	@wraps(func)
	def wrapper(*args, **kwargs):
		"""Wrapper w/ @wraps DocString (This should not be appearing)"""
		print('Wrapper Running:\tw/ @wraps')
		return func(*args, **kwargs)

	return wrapper


@decorator
def fail():
	"""fail DocString"""
	print('Function Running:\t"fail"')


@decorator_wraps
def success():
	"""success DocString"""
	print('Function Running:\t"success"')

for func in fail, success:
	func()
	print(f'Function Name:\t\t"{func.__name__}"')
	print(f'Function DocString:\t"{func.__doc__}"\n')
