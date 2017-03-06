### String Processing

# String literals

# Python allows strings to be enclosed in both single or double quotes, in part because if the string contains either a single...
# ...or double quote, then the opposite kind of quote should be used to enclose the string.

s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = " t-shirts!"
#print s1, s2
#print s3

# Combining strings

# The 'plus' operator combines two strings one after another, with no defaulted space. Spaces can be used in between the end of strings if there should be that much whitespace between the two strings to separate the substrings.
a = ' and '
s4 = "Warren" + a + "Rixner" + ' are nuts!'
# The ',' operator combines two strings, and will default one space per comma between strings, no matter how many additional spaces separate those two strings
print s4

# Characters and slices

# Strings can be subsetted by referencing an integer in the bracket, counting that element in the string using zero based indexing.
print s1[3]
# The len element applied to a string shows how many elements there are in a string
print len(s1)
# String slicing on string 's' can be done by using: s[a:b], and this will return the a up to but not including the b character using zero based indexing.
print s1[0:6] + s2[6:]
print s2[:13] + s1[9:] + s3

# Converting strings
# The str() function converts the inputted argument into a string type.
s5 = str(375)
print s5[1:]
i1 = int(s5[1:])
print i1 + 38
