def say_hi():
	print('hi')
def say_thanks():
	print('thanks')

user = {
	'username': 'Mdev',
	'email':'modev.404@gmail.com',
	'password':'jj1i91391ssw',
	'is_admin':True,
	'is_active':True
}

import platform

def get_platform():
	return {
		'system': platform.system(),
		'machine': platform.machine(),
		'node': platform.node(),
		'processor': platform.processor(),
		'python_version': platform.python_version(),
		'python_build': platform.python_build(),
		'python_compiler': platform.python_compiler(),
		'python_implementation': platform.python_implementation(),
		'meta':dir(platform)
	}