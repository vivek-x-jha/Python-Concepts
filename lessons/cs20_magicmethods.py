def main():
	"""
	Special Methods (i.e. Magic/Dunder Methods)

	1). __repr__
	2). __str__
	3). __add__ - Operator Overloading
	4). __len__
	5). __call__
	"""
	emp1 = Employee('Mary', 'Jane', 55000)
	emp2 = Dunder('Corey', 'Schafer', 50000)
	emp3 = Dunder('Vivek', 'Jha', 60000)

	employees = [emp1, emp2, emp3]

	for emp in employees:
		print(repr(emp))
		print(str(emp))

	assert emp2 + emp3 == 110000
	assert 1 + 2 == 3
	assert 'a' + 'r' == 'ab'

	assert len(emp2) == len(emp2.first + emp2.last)
	assert len('test') == 4

	# emp2()


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Dunder(Employee):

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname()) - 1

    def __call__(self):
        for attribute in sorted(dir(self)):
            print(f'{attribute}: {str(getattr(self, attribute))}')


if __name__ == '__main__':
	main()
