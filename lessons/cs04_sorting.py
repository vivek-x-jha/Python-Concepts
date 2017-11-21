"""
Python Tutorial: Sorting Lists, Tuples, and Objects
https://youtu.be/D3JvDWO-BY4
"""

"""Sorting a list via sorted() function"""

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)
r_li = sorted(li, reverse=True)

print('Original Variable:\t', li)
print('Sorted Variable-f:\t', s_li)
print('Reverse Variable-f:\t', r_li)

"""Sorting a list via .sort() method; Sort method only applies to lists"""

li.sort()

print('Sorted Variable-m:\t', li)

li.sort(reverse=True)

print('Reverse Variable-m:\t', li)

"""Sorting a tuple"""

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)

print('Sorted Tuple:\t\t', s_tup)

"""Sorting a dictionary"""

di = {'name': 'Vivek', 'job': None, 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Sorted Dict:\t\t', s_di)

"""Sorting by absolute value"""
li = [-3, -5, -7, 2, 1, -8, 0]
s_li = sorted(li, key=abs)
print('Absol Sorted Var:\t', s_li)

"""Sorting based on a specific attribute"""


class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.pay)


e1 = Employee('Corey', 37, 50000)
e2 = Employee('Test', 100, 60000)
e3 = Employee('Vivek', 25, 70000)

employees = [e1, e2, e3]  # List of 3 instances of Employee class


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort)
print('Sorted Employees:\t', s_employees)

"""Use lambda function if key function is simple"""

s_employees2 = sorted(employees, key=lambda e: e.name)
print('Sorted Employees-l:\t', s_employees2)

"""Useful function:"""

from operator import attrgetter

s_employees3 = sorted(employees, key=attrgetter('age'))
print('Sorted Employees-a:\t', s_employees3)
