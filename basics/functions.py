def say_hello(name:str):
	print("Hello {}".format(name))
	
say_hello('Mdev')

def calculate_sum(a:float, b:float)->float:
	"""
	:param a: is a float number and must be greater than 0
	:param b: is a float number and must be greater than 0
	:return: sum of a, b the value type is a float
	"""
	if a <=0 or b<=0:
		raise ValueError('a and b must be greater than 0')
	return a+b

try:
	print(calculate_sum(1,-2))
except ValueError as e:
	print(e)
	
def calculate_weekly_salary(days_attended:int,hr_attended:int,per_hr:float)->float:
	pass