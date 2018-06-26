print('in sha1sum.py')

from hashlib import sha1



def string2sha1sum(textToHash):
	return sha1(textToHash).hexdigest()

print(string2sha1sum(''))
#da39a3ee5e6b4b0d3255bfef95601890afd80709