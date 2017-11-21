"""
Programming Terms: Mutable vs Immutable
https://youtu.be/5qQQ3yzbKp8
"""

# An immutable object is an object whose state cannot be modified after it is created

"""1st example is a string"""
a = 'Vivek'
print(a)
print(f'Address of a is: {id(a)}')

"""But can still reassign value to diff memory"""
a = 'John'
print(a)
print(f'Address of a is: {id(a)}')

"""Lists are mutable"""
a = [1, 2, 3, 4, 5]
print(a)
print(f'Address of a is: {id(a)}')

a[0] = 6
print(a)
print(f'Address of a is: {id(a)}')

"""HTML example"""
employees = ['Corey', 'John', 'Rick', 'Steve', 'Carl', 'Adam']

output = '<ul>\n'

for employee in employees:
    output += f'\t<li>{employee}</li>\n'
    print(f'Address of output is {id(output)}')  # This shows how each new string concatenation creates a new memory block

output += '</ul>'

print(output)
print('\n')
