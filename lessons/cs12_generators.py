"""
Python Tutorial: Generators - How to use them and the benefits you receive
https://youtu.be/bD05uGo_sVI
"""
import os
import psutil
from pympler import summary, muppy
import random
import resource
import sys
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


def memory_usage_resource():
    rusage_denom = float(2 ** 10)
    if sys.platform == 'darwin':
        # ... it seems that in OSX the output is different units ...
        rusage_denom *= rusage_denom
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / rusage_denom
    return mem


if __name__ == '__main__':
    print(f'Memory (Before): {memory_usage_resource():.03f} Mb')

    num = 10 ** 6

    # t0 = time.clock()
    # people = people_list(num)
    # delta = time.clock() - t0

    t0 = time.clock()
    people = people_generator(num)
    delta = time.clock() - t0

    print(f'Memory (After) : {memory_usage_resource():.03f} Mb')
    print(f'Took {delta} sec')
