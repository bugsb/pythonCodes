class Emp:

	def __init__(self,first,last):
		self.first = first
		self.last = last
		self.full = first + last


	def __repr__(self):
		
		return "{} - {}".format(self.first,self.last)

	
	def __str__(self):
		
		return self.full



emp1 = Emp('Manishi','Anand')

print(emp1)						# Will call __str__ implicitly if no __str__ then __repr__ is called
print(str(emp1))				
print(repr(emp1))