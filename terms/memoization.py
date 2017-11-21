"""
Programming Terms: Memoization
https://youtu.be/a7EjmdQzPqY
"""

"""
Memoization is an optimation technique used primarily 
to speed up computer programs by storing the results of 
expensive function calls and returning the cached result 
when the same inputs occur again
"""
ef_cache = {3: 9}


def sq(num):

    square = num * num
    ef_cache[num] = square

    return square


def sq_memoize(num):

    if num in ef_cache:
        return ef_cache[num]

    square = num * num
    ef_cache[num] = square

    return square


if __name__ == '__main__':
	sq(3)
	sq_memoize(3)
