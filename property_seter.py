class Emp:

	def __init__(self,first,last):
		self.first = first
		self.last = last

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first,self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	@fullname.setter
	def fullname(self,name):
		first,last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Delte name !')
		self.first = None
		self.last = None



emp1 = Emp('mani','bhai')
emp1.fullname = "Manishi Anand"      #Will call @fullname.sertter

print(emp1.email)
print(emp1.fullname)
del emp1.fullname          # Will call @fullname.deleter
