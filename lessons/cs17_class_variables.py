class Employee:
	emp_counter = 0
	raise_amount = 1.04

	def __init__(self, firstname, lastname, wage):
		self.first = firstname
		self.last = lastname
		self.pay = float(wage)
		self.email = f'{firstname}.{lastname}@company.com'

		Employee.emp_counter += 1

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay *= self.raise_amount


def main():
	"""
	Class Attributes (i.e. Class Variables):

	1). Creates 2 unique instances of 'Employee' class
	2). Increments 'emp_counter' class attribute every instantiation
	3). Sets 'raise_amount' class attribute through an instance (Note that it changes the value ONLY for emp1)
	4). Prints instances' namespaces (Note 'raise_amount' now appears directly in 'emp1' namespace)
	"""
	emp1 = Employee('Vivek', 'Jha', 100000)
	emp2 = Employee('Mubuntu', 'M', 100000)

	employees = [emp1, emp2]
	assert Employee.emp_counter == len(employees)

	emp1.raise_amount = 1.05
	assert emp2.raise_amount == Employee.raise_amount == 1.04

	for emp in employees:
		for k, v in emp.__dict__.items():
			print(f'{k}: {v}')
		emp.apply_raise()

		print(f"\n{emp.fullname()}'s after-raise pay:\t${emp.pay:.2f}\n")

	# print(Employee.__dict__)


if __name__ == '__main__':
	main()
