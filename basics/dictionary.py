car = {
	'brand':'Ford',
	'model':'Mustang',
	'year':1964
}
print(car)
print(type(car))
print(car.keys())
print(car.values())
print(car['year'])
print(car['model'])
print(len(car))

student = {
	'name':'Osama',
	'age':23,
	'courses':['Python','JS','React'],
	'is_active':True,
}

keys = student.keys()
values = student.values()

print(student)
print(student.get('courses'))
print(student['is_active'])
print('before update',[keys,values])
student['location'] = 'KM4'
student['is_active'] = False
print('after update',[keys,values])
print('Items ',student.items())
if 'is_active' in student:
	print('is_active key is in student')

print(dict(color='Red',type='Electric',price=20,period='2m'))

print(car)
car['year'] = 2003
print(car)
car.update({'model':'Electric'})
print(car)
car['color'] = 'black'
print(car)
car.pop('color')
print(car)
del car['model']
print(car)
car.popitem()
print(car)
car.clear()
print(car)