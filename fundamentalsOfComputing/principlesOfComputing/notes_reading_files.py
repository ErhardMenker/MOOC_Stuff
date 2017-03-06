### Reading files from the network

# Opening a file using the "r" is for read mode, "w" for write. This does not work in CodeSkulptor.

import urllib2
import codeskulptor

FILENAME = "examples_files_dracula.txt"

url = codeskulptor.file2url(FILENAME)
netfile = urllib2.urlopen(url)

data = netfile.read()
print data
print type(data)

for line in netfile.readlines():
    print line