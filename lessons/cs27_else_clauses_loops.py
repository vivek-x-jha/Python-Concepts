"""
Python Tutorial: Else Clauses on Loops
https://youtu.be/Dh-0lAyc3Bc
"""


def find_index(to_search, target):
    """Finds index of element in list using for/else"""
    for i, value in enumerate(to_search):
        if value == target:
            break
    else:  # "else:" == "if no break:" (In context of for/while loops)
        return -1
    return i  # Note: when loop breaks, it skips else clause


if __name__ == '__main__':
    my_list = ['Corey', 'Vivek', 'John']
    target = 'Sam'
    index_location = find_index(my_list, target)

    print(my_list)
    print(f'Location of {target} is index: {index_location}')
