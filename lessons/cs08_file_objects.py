"""
Python Tutorial: File Objects - Reading and Writing to Files
https://youtu.be/Uh2ebFW8OYM
"""

"""Opening files via open()"""

f = open('test.txt', 'r')

print(f.name)

f.close()

"""Opening files via context manager (This is better way, r/c automatically closes file)"""

with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

"""Different way of formatting the lines"""

with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

"""Import first 3 lines of file"""

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')

"""Efficiently read contents of a file line by line"""

with open('test.txt', 'r') as f:

    for line in f:
        print(line, end='')

"""Efficiently read contents of a file character by character"""

with open('test.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)

"""Writing to files"""

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

"""Copying a txt file to a new file"""

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

"""Copying picture file to a new file"""

with open('/Users/vivekjha/Pictures/Raiders.jpg', 'rb') as rf:
    with open('Raiders_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)
