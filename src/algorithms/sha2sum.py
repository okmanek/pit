from hashlib import sha256

print('in sha256sum.py')



def string2sha2sum(textToHash):
	return hashlib.sha256(textToHash).hexdigest()

#e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855