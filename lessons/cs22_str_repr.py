"""
Python Tutorial: str() vs repr()
https://youtu.be/5cvM-crlDvg
"""
import datetime
import pytz

a = [1, 2, 3, 4]
b = 'sample string'

print(str(a))
print(repr(a))

print(str(b))
print(repr(b))

c = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
d = str(c)

print(f'str(c): {str(c)}')
print(f'str(d): {str(d)}')

print(f'repr(c): {repr(c)}')
print(f'repr(d): {repr(d)}')
