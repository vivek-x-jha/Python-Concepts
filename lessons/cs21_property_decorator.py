def main():
	"""
	Property Decorators - Getters, Setters, and Deleters

	1). Getters use '@property' decorator to turn method into an attribute
	2). Setters allow changing getter value, while also updating the values of any attributes used
	3). Deleters turn attributes into 'None'
	"""
	emp = Employee('Vivek', 'Jha')

	assert emp.first == 'Vivek'
	assert emp.last == 'Jha'
	assert emp.fullname == 'Vivek Jha'
	assert emp.email == 'Vivek.Jha@company.com'

	emp.fullname = 'John Snow'

	assert emp.first == 'John'
	assert emp.last == 'Snow'
	assert emp.fullname == 'John Snow'
	assert emp.email == 'John.Snow@company.com'

	del emp.fullname

	assert emp.first is None
	assert emp.last is None
	assert emp.fullname == 'None None'
	assert emp.email == 'None.None@company.com'


class Employee:
	def __init__(self, firstname, lastname):
		self.first = firstname
		self.last = lastname

	@property
	def email(self):
		return f'{self.first}.{self.last}@company.com'

	@property
	def fullname(self):
		return f'{self.first} {self.last}'

	@fullname.setter
	def fullname(self, name):
		firstname, lastname = name.split(' ')
		self.first = firstname
		self.last = lastname

	@fullname.deleter
	def fullname(self):
		self.first = None
		self.last = None


if __name__ == '__main__':
	main()
