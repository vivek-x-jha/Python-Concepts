def main():
	"""
	Demonstrates how to use the namedtuple csvdata structure

	with regular tuples, it isn't obvious what the csvdata represents:
	blue = (0, 0, 255)
	could represent rgb, hue, saturation, etc...

	but dictionaries are mutable and lengthy to type:
	black = {'red': 0, 'green': 0, 'blue': 0}

	"""
	from collections import namedtuple

	Color = namedtuple('Color', ['red', 'green', 'blue'])

	blue = Color(blue=255, green=0, red=0)
	white = Color(255, 255, 255)


if __name__ == '__main__':
	main()
