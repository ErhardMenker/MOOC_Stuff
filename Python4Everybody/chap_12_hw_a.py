""" PROGRAM TO PARSE HTML AND SUM UP NUMBERS IN SELECTED LINES CONTAINING AN ANCHOR TAG"""

# Define global variable
FILE = "http://python-data.dr-chuck.net/comments_204626.html"

# Import relevant modules
import urllib
import re

# Loop through each line in the HTML, parsing with regex
fhand = urllib.urlopen(FILE)
# Initialize an empty list
t = list()

for line in fhand:
    line = line.rstrip()
    relevant_html = re.findall('<tr><td>\S*</td><td><span\sclass="comments">([0-9.]+)</span></td></tr>', line)
    # Append non-empty lines that contain the parsed numbers into a list
    if len(relevant_html) > 0:
        t.append(relevant_html)

# Initialize an accumulator equal to zero
sum = 0
# Loop through list containing one element lists
for element in t:
    # Extract element from the one element list it is bounded within
    for value in element:
        value = int(value)
        sum = value + sum
print(sum)