# Program to read text from on the web, including the text file's metadata

# Import socket library
import socket
# Define socket variable
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect socket to the web page
mysock.connect(('www.pythonlearn.com', 80))
# Request data back using complicated conjunction of GET and host definition because now file uses HTTP 1.1 (thank God for urrlib!)
mysock.send('GET /code/intro-short.txt HTTP/1.0\nHost: www.pythonlearn.com\n\n')

while True:
    # Receive data in up to 512 character chunks from the socket
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()

#use urllib library to import same text file and count up each word in a dictionary

import urllib

# create connection to the text file:
fhand = urllib.urlopen('http://www.pythonlearn.com/code/intro-short.txt')
# initialize empty dictionary:
count = dict()
for line in fhand:
    line = line.split()
    for word in line:
        count[word] = count.get(word, 0) + 1
print (count)

        
    


    
