#!/usr/bin/env python
import src.algorithms.sha1sum
import src.algorithms.sha256sum
log = True

print('in test')

def test_algorithms():
	#testing sha1sum
	assert (src.algorithms.sha1sum.string2sha1sum('') == 'da39a3ee5e6b4b0d3255bfef95601890afd80709')


test_algorithms()