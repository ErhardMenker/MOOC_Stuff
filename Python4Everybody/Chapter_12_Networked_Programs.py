### Chapter 12: Networked Programs ###

## Motivation
# There are many different sources of information when considering the internet.
# Data can be read through the web and parsed.
# Transport Control Protocol (TCP) can be thought of as the proper way a user's computer should interact with the server's computer in requesting and pulling data, and the main form of TCP is HTTP 

## HyperText Transport Protocol - HTTP
# HyperText Transport Protocol (HTTP) is a common method of retrieving web data.
# An HTTP URL (uniform resource locator) contains three important components (protocol, host, document) of the form: http://hostname/doctitle (protocol is http, host is hostname, and document is doctitle)
# The network protocol that powers the web is actually quite simple.
# Python has support called "sockets" that creates network connections and retrieves/sends data over those sockets.
# A socket is the endpoint between two computers that bidirectionally share data.
# A socket allows use of inter-connected computers like a filehandle allows usage of a file.
# A socket allows for a two-way connection between two applications that sends data in either direction (a socket library exists).
# Reading and writing can be done from the same socket...
# ...writing to a socket sends the application to the other end of the socket...
# ...while reading from the socket gives the data with which the other applicatoin has been sent.
# Warning: reading a socket when the program on the other end has not sent any data results in nothing, with no error message.
# A properly written socket has a protocol, or a set of precise rules that determines in what order operations occur.
# Proper protocols are determined by the Internet Engineering Task Force (IETF).
# Coordination must occur from both ends of the socket to make sure actions don't occur out of order.
# A port is a number that indicates which application you are contacting when you make a socket connection to a server (like different telephone extensions resulting in ability to contact different phones)... 
# ...(email is port 25, web traffic port 80), allowing the existence of multiple network acpplications on the same server.
# To request a document from a web server for this class's examples, make a connection to the www.py4inf.com server on port 80, sending a line of the form:GET http://www.py4inf.com/code/romeo.txt HTTP/1.0 (second parameter is the requested web page) 
# The request-response cycle is the process of asking for data from the internet from a user's computer and waiting for the internet source to be able to send it back to the user's computer.
# Example: clicking a URL on a page is the request, when it actually loads (after receiving the data) is the response.

# Syntax for importing data using the socket library:
import socket
# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect socket to this website at this port
mysock.connect(('www.py4inf.com', 80)) # connect to this website at this port

## The World's Simplest Web Browser
# For application protocols the request-response cycle involves using a GET command and then inputting the request URL, and then waiting for that URL's information to be returned

# Here is a program showing HTTP protocol to connect to a web server and request a document

# Import socket module
import socket

# Create socket called "mysock"
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Make a connection to port 80 on the server www.py4inf.com
mysock.connect(('www.py4inf.com', 80))
# Request to get back this text file at the connected socket page
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

# After blank line containing metdata, prints data so long as there is non-white space on a given line, then break
while True:
    # Receive data in up to 512 character chunks from the socket
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data

mysock.close()

break

# The above program returns characteristics of the document (headers), such as stating the Content_type is a text/plain file...
# ...before reading out the text in the format requested.

## Retrieving an Image over HTTP
# A similar program can retrieve an image across using HTTP by accumulating the data in a string, trimming off headers, and saving the image data to a file:

import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
# Including GET is what occurs "behind the hood" when you click on a URL in the socket data request on the web
mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

count = 0
picture = "";
while True:
    # Will return up to 5120 characters each time the recv() method is called (often times it is less)
    data = mysock.recv(5120)
    if ( len(data) < 1 ) : break
    # time.sleep() method waits a quarter of a second after each call so the server can "get ahead" of the data requests before recv() is called again (flow control)
    time.sleep(0.25)
    # Count value sums up how much data has been imported up to that point
    count = count + len(data)
    print len(data),count
    picture = picture + data
    
mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find("\r\n\r\n");
print 'Header length',pos
print picture[:pos]

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg","wb")
fhand.write(picture);
fhand.close()

# The Content-Type header in the output indicates that the body of the document is an image (image/jpeg)
# The amount of characters inputted into the recv() method isn't necessarily how much will actually get transferred,...
# ...either because there aren't that many characters in the location or the buffer hasn't been filled with that many characters when the data are pulled... 
# ...because data can be pulled faster than they are pushed
# Placing buffers between send() and recv() requests (the time.sleep() method) is called "flow control," used to prevent the server from requesting data that isn't ready.

## Retrieving web pages with urllib
# Python has a special library designed to support HTTP protocol for data retrieval because it is so common called urllib.
# Sending and receiving data over HTTP can be done with the socket library (above), but is more easily done using the urllib library.
# urllib does not print out the metadata, unlike when using the GET request.
# The urllib library allows treating a web page much like a file...
# ...simply indicate which web page should be retrieved and urllib handles all of the HTTP protocol and header details.
# The urllib.urlopen() method with a web page file input sets an assigned variable as a filehandler equal to the inputted web page.

# Task: read the romeo.txt file using urllib:

# Import urllib library
import urllib

# Establish file handle mapping to the domain
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
# Loop through each line of the web page, as if using the open() command on a text file on disk
for line in fhand:
    print line.strip()
    
#Task: read the romeo.txt file and comput the frequency of each word:

import urllib

# Initialize an empty dictionary
counts = dict()
# Create a file handle
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
# Loop through each line in the file and...
for line in fhand:
    # ...split it into a space delimited list
    words = line.split()
    # For each key (word_...
    for word in words:
        # ...add 1 to its value, or initialize value to 0 if key does not exist yet
        counts[word] = counts.get(word, 0) + 1
print counts

## Parsing HTML and scraping the web
# Scraping occurs when a program pretends to be a web browser and retrieves a web page, then looks at the web page content by parsing methods and then goes back to the web to fetch more data.
# A spider is a web search engine retrieving a page and using that page as a search index to reference similar pages.
# One way to parse HTML is to use regular expressions to repeatedly search for and extract substrings matching a particular pattern.

# Task: parse a given web page and print all substrings that have href="http://" followed by non-whitespace, non-greedily.

import urllib
import read

#html = urllib.urlopen("insert valid link").read()
#links = re.findall('href="(http://.*?)', html)
#for link in links:
#    print link

## Parsing HTML using BeautifulSoup
# Desired data can be missed and undesired data can be caught using regular expressions in HTML when the HTML page is poorly formatted and unpredictable.
# Poorly formatted HTML can be solved using a robust HTML parsing library called BeautifulSoup.
# BeautifulSoup is not built into Python but will work by bringing the BeautifulSoup py file into the same directory as the working file.

import urllib
# Calls out the BeautifulSoup py file in the same folder level as this python program
from BeautifulSoup import *
# Request the file as an input and set it equal to variable ur1
url = input('Enter -')
# Open and read each line in the web page
html = urllib.urlopen(ur1).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
    
# This program prompts for a web address, then opns the web page, reads the data,...
# ...and passes the data to the BeautifulSoup parser, and then retrieves all of the anchor tags and prints out the href attribute for each tag.

## Reading binary files using urllib
# Sometimes it is desirable to retrieve a non-text (or binary) file such as an image/video file.
# The pattern for retrieving binary files is to open the URL, use read to download the entire contents of the document into a string variable (img),...
# ...and then write that information to a local file, as follows:

import urllib
# Read all data at once across the network
img = urllib.urlopen("http://www.py4inf.com/cover.jpg").read()
# Store image file in a filehandle in RAM
fhand = open('cover.jpg', 'w')
# Write to disk as a file called 'img'
fhand.write(img)
fhand.close()

# It might be better to try to break up this task in case the file is very large:

import urllib

img = urllib.urlopen("http://www.py4inf.com/cover.jpg")
fhans - open('cover.jpg', 'w')
size = 0
while True:
    # write 100000 characters at a time before...
    info = img.read(100000)
    if len(info) < 1: break
    size += len(info)
    # ...writing out positive sized lines to disk
    fhand.write(info)
    
print size, 'characters copied.'
fhand.close()