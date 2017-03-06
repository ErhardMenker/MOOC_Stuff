### Assertions

# Assertions check to make sure conditions are held in your program.
# Assertions throw errors if a condition does not hold in a program.
# Assert is a function in Python, and is called by...
# assert <logical_condition>, <error_if_False> throws an error if the logical condition does not hold... 
# ...where the logical_conditional can be compound.
# If the logical condition holds, the assert statement is not evaluated.

import math
def hyp(s1, s2):
	hyp = math.sqrt(s1 ** 2 + s2 ** 2)
	assert (hyp > s1 and hyp > s2), "hypothesis too long"
	assert hyp < (s1 + s2), "hypothesis too short"
	#only will reach this return if neither of two previous Bools hold
	return hyp

print hyp(3, 7)
s