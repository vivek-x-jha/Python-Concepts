"""
Python Tutorial: String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates
https://youtu.be/vTX3IwquFkc
"""

import datetime

person = {'name': 'Vivek', 'age': 25}
person_list = ['Vivek', 25]

"""Messy Concatenation of terms"""
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

"""Using Format method"""
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)

"""Can label parameters passed into format() as 0,1,2,..."""
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)

"""Useful when need to repeat given parameter(s)"""
tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

"""How to format elements of a dictionary"""
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)

"""How to format elements of a list"""
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(person_list)
print(sentence)

"""How to format attributes of a class"""


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

"""How to format using a key"""
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
print(sentence)

"""How to format if using just 1 dictionary"""
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

"""Can format output using : operator"""
for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

"""September 24, 2016"""
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

"""September 24, 2016 on a Saturday and was the 268th day of the year."""
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j}th day of the year.'.format(my_date)
print(sentence)
