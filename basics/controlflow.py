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

x = 6
y = 8

if x < y and is_active:
	print(x,'is less than',y,sep=' ')
if x > y or is_active:
	print('x is not greater than',x,y,'this is because of or condition',sep=' ')
	

size= 32
width = 33

if not size >= width:
	print('size is less than width')

if size:
	pass

weather = 'hot'

match weather:
	case 'rainy':
		print('rainy')
	case 'snow':
		print('Snowing is so cool')
	case 'sunny' | 'cloudy':
		print('Sunny or cloudy is so calm')
	case _:
		print(weather,'is not available')