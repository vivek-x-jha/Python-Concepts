def main():
	"""
	Inheritance - Creating Subclasses

	Class Diagram:

	Employee -> Developer
	         -> Manager

	1).
	"""
	subclasses = [Manager, Developer]

	emp1 = Employee('John', 'Snow', 60000)
	dev1 = Developer('Arya', 'Stark', 80000, 'Python')
	dev2 = Developer('Jane', 'Doe', 80000, 'C++')
	mgr1 = Manager('Vivek', 'Jha', 100000)

	subinstances = [mgr1, dev1, dev2, emp1]

	"""SubClass attributes overide any inherited class attributes of same name"""
	# for inst in instances:
	# 	inst.apply_raise()
	# 	assert inst.pay ==
	dev1.apply_raise()
	print(emp1.pay)
	print(dev1.pay)

	"""How to use inherited classes"""
	mgr1.print_emps()
	mgr1.add_emp(dev2)
	mgr1.add_emp(emp1)
	mgr1.remove_emp(dev1)
	mgr1.print_emps()

	"""Check if object is instance of a class"""
	for subclass_inst in subinstances:
		for subclass in subclasses:
			if isinstance(subclass_inst, subclass):
				print(f'{subclass_inst} is in {subclass.__name__}')
			else:
				print(f'{subclass_inst} is not in {subclass.__name__}')

	"""Check if class is subclass of a class"""


class Employee:
	raise_amt = 1.04

	def __init__(self, firstname, lastname, wage):
		self.first = firstname
		self.last = lastname
		self.pay = wage
		self.email = f'{self.first}.{self.last}@company.com'

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = float(self.pay * self.raise_amt)

	def isinst(self, cls):
		if isinstance(self, cls):
			return True


class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, firstname, lastname, wage, prog_lang):
		super().__init__(firstname, lastname, wage)
		self.language = prog_lang


class Manager(Employee):
	def __init__(self, firstname, lastname, wage, emps=None):
		super().__init__(firstname, lastname, wage)
		if emps is None:
			self.employees = []
		else:
			self.employees = emps

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())


if __name__ == '__main__':
	main()
