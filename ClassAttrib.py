class Container:
	"""docstring for Container"""
	Container_id = 1337
	def __init__(self, owner_id,contents):
	
		self.owner_id = owner_id
		self.contents = contents
		self.Container_id = Container.Container_id     # Container_id will be incremented automatically
		Container.Container_id += 1    				   # After every instance created




c1 = Container('MAC','YAML')

print(c1.Container_id)

c2 = Container('OSX','PY')

print(c2.Container_id) 