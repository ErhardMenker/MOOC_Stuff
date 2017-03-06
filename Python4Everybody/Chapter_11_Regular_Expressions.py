###Chapter 11: Regular Expressions###

##Regular Expressions Intro
#Regular expressions are a set of characters used to match strings, standard across programming languages.
#The regular expression library must be imported before use, called: read
import re #imports the regular expression library
#The re.search('regex', 's') method tests to see if the string inputs matches a regular expression denoted regex (similar to using find() for strings), returning a Boolean if at least one value is found.
#The re.findall('regex', 's') method looks through a string s and returns all substrings (part of regex in parenthesis) satisfying the entire regex in a list, bounded in quotes (list is empty if none is found)
#The search function is the simplest use of regular expressions:
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip() #strip off rightward white space
    if re.search('From:', line):
        print(line) #only print off lines that have 'From:' as a part of the line
#This program is trivial, as using line.find("From:") could have accomplished the same goal
#The power of regular expressions comes when special characters are added to the search string to allow more precise control of which lines match the string.
#Example: the caret character used in regular expressions only searches the beginning of the line.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line) #if iterated line starts with From:...
        print(line) #...print that line
#This program produces the same result as when the startswith() method is used.

##Character Matching in Regular Expressions
#Special characters allow efficient matching when regular expressions are used.
#The period character matches any character at that point in the search.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:', line): #evaluates to true if line starts with 'F', followed by any 2 charaters, followed by 'm:'
        print(line)
#The rcharacter '*' matches zero or more characters in a location while '+' matches one or more characters.
#In matching, the character '.*' matches a character zero or times in a location while '+' matches the character one or more times.
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line): #evaluates to true if line starts with 'From:', followed by an @ sign at least one character to the right of the ':'
        print(line)
#Repeated wild card ('+' and '*') are 'pushy', in the sense that they include a lot of potential matches and may return unwanted text
#The findall() method extracts all substrings which matches a regular expression.
import re
s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
lst = re.findall('\S+@\S+', s) #searches the second string argument and returns a list of strings that look like email addresses
print(lst) #does not match @2pm, because there are no non-whitespace characters before the '@'
#The regular expression looks for substrings that have at least one non-whitespace character, followed by an @ sign, followed by one more non-whitespace character
#The "\S+" matches as many non-white space characters as exist.
#The translation of '\S+@\S+' is therefore: find a substring where there is an '@' preceded and followed by any positive amounts of non-whitespace characters
#The [] option in regular expression allows specifying multiple 'or' options when parsing
[a-ZA-Z0-9]\S*@\S*[a-zA-Z] #looks for substrings starting with a single lowercase letter, upper case letter, or number ([a-zA-Z0-9]), followed by zero or more non-blank characters ("|S*"), followed by an @, followed by an uppercase or lowercase letter

##Combining Searching and Extracting
#Extract lines that have the following structure: X-DSPAM-Confidence: 0.8475 ; X-DSPAM-Probability: 0.0000 :
^X-.*: [0-9.]+ #translation: look for lines that start with "X-", followed by zero or more characters (".*"), followed by a colon (":") and then a space, then one or more characters that are either a digit (0-9) or a period (the "." is not  a wildcard between square brackets)
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9. ]+)', line) #extract all lines of above form, but only subset the numbers (indicated by bounding them in parenthesis)
    if len(x) > 0:
        print(x)
#Consider a line of the form: Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
#Here is a program that extracts the integer numbers at the end:
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details:.*rev=([0-9]+)', line) #Find lines that starts with Details:, followed by zero or more intermediary characters, followed by rev=, and then followed by one or more digits, which is extracted into x (including as many digits as possible)    
    if len(x) > 0:
        print(x)
#Consider lines of form: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008, extract the hours:
^From .* ([0-9][0-9]) #finds lines starting with From, followed by a space, followed by any intermediary characters and then a space, followed by two consecutive digits and then a colon, extracting the two digits by virtue of the comma

##Escape Character
#We can indicate that we weant to simply match a character by using a backslash:
import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9. ]+', x) #subsets parts of the string with a digit followed by a period followed by at least one character
#By prefixing the '$' with a '\', we match the dollar sign in the input string instead of matching the "end of the line." 
#Inside of brackets, a period is a period and not a wildcard.

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y) #returns: ['2', '19', '42']
y = re.findall('[AEIOU]+', x) 
print(y) #returns [], no capital vowels exist in mother string

##Summary of Regular Expressions
#Regular expressions are search strings with special characters that communicate wishes to the regular expression system as to what defines "matching" and what is to be extracted from matched strings.
#The capability of using regular expressions is called by: import re
#Greedy matching returns as large a string as possible that satisfies the RE logic, (example: going from 'From:' to a colon in a string with two colons will return from 'From:' to the second colon)
# ^ matches the beginning of the line
# $ matches the end of the line
# . matches any character (wildcard)
# \s matches a whitespace character
# \S matches a non-whitespace character (opposite of \s)
# * matches the preceding character(s) zero or more times, matching greedily
# *? matches the character(s) preceding zero or more times, matching non-greedily
# + matches the preceding character(s) one or more times, matching greedily
# +? matches the character(s) preceding one or more times, matching non-greedily
# [aeiouz] matches a single character as long as it is in the set (this set would match 'a', 'e', 'i', 'o', 'u', or 'z', but nothing else) 
# [a-z0-9] matches a range of characters using the minus sign, this being lower case digit (a-z) or digit (0-9)
# [^A-Za-z] first character in a set being a carat inverts the logic, so in here match a single character that is anything other than an upper or lower case letter
# () is ignored for the purpose of matching, but returns the subset of the matched string (that which is bounded in parenthesis) rather than the whole string when findall() is called
# \b matches the empty string, but only at the start or end of a word
# \B matches the empty string, but not at the start or end of a word
# \d matches any digit (equivalent to calling [0-9])
# \D matches any non-digit character (equivalent to the set [^0-9])
# Appending a '\' to the beginning of a character means to actually match that character, that it is not a regex if it is normally a regex