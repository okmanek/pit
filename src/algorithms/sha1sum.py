from hashlib import sha1

if log:
	print('in sha1sum.py')



def string2sha1sum(textToHash):
	return sha1(textToHash).hexdigest()