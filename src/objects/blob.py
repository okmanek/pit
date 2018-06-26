print('in blob.py')

from object import Object

#hashlib.sha1("").hexdigest()

class Blob(Object):
	def __init__(self):
		print('blob created')

	def string2blob