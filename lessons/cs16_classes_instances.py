def main():
	"""
	Classes and Instances:

	1). Creates 2 unique instances of 'Employee' class
	2). Prints various instance attributes
	3). Shows equivalent ways of calling a method
	"""
	emp1 = Employee('Vivek', 'Jha', 100000)
	emp2 = Employee('Mubuntu', 'M', 100000)

	print(emp1.pay)
	print(emp1.email)
	print(emp2.email)

	assert emp1.fullname() == Employee.fullname(emp1)


class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return f'{self.first} {self.last}'


if __name__ == '__main__':
	main()
