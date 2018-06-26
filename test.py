#!/usr/bin/env python
import src.algorithms.sha1sum

print('in test')

#assert 2 + 2 == 5, "no"
#assert 2 + 2 == 5, "yes"

assert (3 > 2), "3 is bigger"

#testing sha1sum
assert (src.algorithms.sha1sum.string2sha1sum('') == 'da39a3ee5e6b4b0d3255bfef95601890afd80709')