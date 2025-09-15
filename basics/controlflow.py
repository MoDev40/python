a = 33
b = 200
if a < b:
	print(a,'is less than',b,sep=' ')
if b > a:
	print(b,'is greater than',a,sep=' ')
city = 'New York'.lower()

if city == 'New York':
	print('City is',city)
elif city == 'New York'.lower():
	print('This is the real',city)
else:
	print('No available city')
	
is_active = True

print('Active') if is_active else print('Inactive')