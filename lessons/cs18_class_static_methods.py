from datetime import date
import calendar


class Employee:
	raise_amt = 1.04

	def __init__(self, firstname, lastname, wage):
		self.first = firstname
		self.last = lastname
		self.pay = float(wage)
		self.email = f'{self.first}.{self.last}@company.com'

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split(', ')
		return cls(first, last, float(pay))

	@classmethod
	def set_raise_amt(cls, amt):
		cls.raise_amt = amt

	@staticmethod
	def isWorkday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


def main():
	"""
	Class/Staticmethods:

	Classmethod - methods performing some action on the class
				- takes 'cls' as 1st arg (not 'self')
				- can be used as alternative constructors

	Staticmethod - used to classify functions logically connected to a class
				 - does not take 'self' or 'cls' as an argument
				 - if class has too many staticmethods, take them out and import as modules

	1). Uses 'from_string' classmethod to parse 'emp_str' & instantiate 'Employee'
	2). Calls 'set_raise_amt' classmethod to change 'raise_amt' class attribute
	3). Uses 'isWorkday' staticmethod to check if it's a workday
	"""
	emp_str = 'John, Snow, 1200000'

	emp1 = Employee('Vivek', 'Jha', 100000)
	emp2 = Employee('Mubuntu', 'M', 100000)
	emp3 = Employee.from_string(emp_str)

	assert emp3.first == 'John'
	assert emp3.last == 'Snow'
	assert emp3.pay == 1200000
	assert emp3.email == 'John.Snow@company.com'
	assert emp3.raise_amt == 1.04

	Employee.set_raise_amt(1.05)

	emp_objects = [emp1, emp2, emp3, Employee]
	for employee in emp_objects:
		assert employee.raise_amt == 1.05

	today = date.today()  # Mon = 0, Tues = 1, ...
	day = calendar.day_name[today.weekday()]

	if Employee.isWorkday(today):
		print(f'\nToday is {day} - Back to work!')
	else:
		print(f'\nToday is {day} - No work today!')


if __name__ == '__main__':
	main()
