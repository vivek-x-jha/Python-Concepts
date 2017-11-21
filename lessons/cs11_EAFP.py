"""
Python Tutorial: Duck Typing and Asking Forgiveness, Not Permission (EAFP)
https://youtu.be/x3v9zMX1s4s
"""


def main():
	"""Compares result of 3 approaches below"""
	d = Duck()
	p = Person()
	for inst in d, p:
		bad(inst)
		better(inst)
		best(inst)
		print((dir(inst)))
		print('\n')


def bad(thing):
	"""Not Duck-Typed (Non-Pythonic)"""
	if isinstance(thing, Duck):
		thing.quack()
		thing.fly()
	else:
		print('bad called: This has to be a Duck!')


def better(thing):
	"""LBYL: "Look before you leap" (Non-Pythonic)"""
	if hasattr(thing, 'quack'):
		if callable(thing.quack):
			thing.quack()

	if hasattr(thing, 'fly'):
		if callable(thing.fly):
			thing.fly()

def best(thing):
	"""EAFP: Easier to ask forgiveness than permission i.e. Duck-Typed (Pythonic)"""
	try:
		thing.quack()
		thing.fly()
		thing.bark()
	except AttributeError as e:
		print(e)


class Duck:

	def quack(self):
		print(f'{type(self).__name__}.quack called: Quack, quack')

	def fly(self):
		print(f'{type(self).__name__}.fly called: Flap, Flap!')


class Person:

	def quack(self):
		print(f"{type(self).__name__}.quack called: I'm Quacking Like a Duck!")

	def fly(self):
		print(f"{type(self).__name__}.fly called: I'm Flapping my Arms!")


if __name__ == '__main__':
	main()
