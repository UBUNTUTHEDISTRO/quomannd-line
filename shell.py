while True:
	cmdinput = input('? ')
	
	if cmdinput == 'help':
		print('here is a list of commands')
		print('dir')
		print('about')
		print('exit')
	
	elif cmdinput == 'dir':
		print('No files in /pythonFS/')
	
	elif cmdinput == 'about':
		print('This python file is a shell,')
		print('written by me.')
		print('thx tutorials!')
	
	elif cmdinput == 'exit':
		print('cya!')
		exit()
