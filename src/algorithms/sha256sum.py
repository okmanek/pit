from hashlib import sha256

if log:
	print('in sha256sum.py')



def string2sha256sum(textToHash):
	return hashlib.sha256(textToHash).hexdigest()

