""" Program to tabulate emails in a SQLite3 DB by count """

import urllib
import re
import sqlite3

my_dict = dict()

fhand = urllib.urlopen('http://www.pythonlearn.com/code/mbox.txt')
# loop through online text file and extract institution names
for line in fhand:
    line = line.strip()
    # if no email address exists in this line, skip iteration:
    if not re.search('^From:', line): 
        continue
    else:
        inst = re.findall('@(.+)', line)
    # iterate through one element list (convert content to hashable string)
    for elem in inst:
        my_dict[elem] = my_dict.get(elem , 0) + 1

print(my_dict)        

# import resulting dictionary into a SQLite3 database
conn = sqlite3.connect('email_counter.sqlite')
cur = conn.cursor()

# drop Tracks table if it exists
cur.execute('DROP TABLE IF EXISTS Counts')

# create table structure
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# loop through dictionary and insert content into table
for inst, total in my_dict.items():
    cur.execute('INSERT INTO Counts (org, count) VALUES (?,?)', (inst, total))

conn.commit()    
conn.close()    


    




