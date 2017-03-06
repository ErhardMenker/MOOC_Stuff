""" PROGRAM TO PARSE HTML LINKS, FINDING THE SPECIFIED COUNTED INSTANCE OF A CERTAIN LINK IN A SPECIFIED
POSITION AND GOING TO THAT HTML PAGE AND REPEATING THE PROCESS AS MANY TIMES AS THE COUNT SPECIFIES """

# Define global variable
FILE = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Zacharie.html "
COUNT = 7
POSITION = 18

# Import relevant modules
import urllib
import re

# Loop through each line in the HTML, parsing with regex
count_current = 1
val = 0

while count_current <= COUNT:
    position_current = 1
    fhand = urllib.urlopen(FILE)
    for line in fhand:
        if re.search("n-data/data/known_by_[\S]*.html", line):
            position_current += 1
            if position_current == POSITION + 1:
                names = re.findall("n-data/data/known_by_([\S]*).html", line)
                count_current += 1
                for name in names:
                    FILE = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_" + name + ".html"
                    print(FILE)


        