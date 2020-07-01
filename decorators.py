def decor_fun(original_fun):
	
	def wrapper_fun(*args):
		
		print('Added functionality')
		return original_fun(*args)
	return wrapper_fun




@decor_fun
def display():
	print("This is display functionality")


@decor_fun
def more_fun(arg):
	print('Added More functionality with {}'.format (arg))

display()
more_fun('arg')	
	
ipt = input()

