from object import Object

print('in blob.py')



#hashlib.sha1("").hexdigest()

class Blob(Object):
	def __init__(self):
		print('blob created')

	def string2blob