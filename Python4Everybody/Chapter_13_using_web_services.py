### Chapter 13: Using Web Services ###

## Motivation
# Once HTTP was retrievable and parsable, documents were produced in the browser made...
# ...with the purpose of being consumed by other programs, so standardized formats needed to be created.
# Two covered formats exchange data across the web, "eXtensible Markup Language" (XML) and "JavaScript Object Notation" (JSON).
# Converting Python syntax into a format that can be readable on the web is serializing, while the reverse process of...
# ...converting that data to native Python is de-serializing.
# Therefore, Python scripts to be shared over the web are serialized into XML or JSON and then deserialized by users back into Python.

## eXtensible Markup Language (XML)
# XML is similar to HTML but better structured.
# XML states a top tag or "person," and maps other tags to that person's characteristics.
# For example, XML can state a person and map characteristics of that person such as the name, number, email.
# The characteristics are the tag, while the tag's value is its node.
# The tags are on the outside, while the corresponding node is embedded on the inside between the greater/less than signs.
# If a tag includes tags embedded within it, it is a complex element. If the tag only includes text within, it is simple.
# The inside of a tag is bounded by a start tag and an end tag (same title, but shows what is bounded as the tag's content)
# Tag creations can state the character type of its corresponding node (such as integer, date, character, and so on)
# Attributes can be included within a start tag in XML. This is a key-value pair (such as within the phone tag, mapping type=INTL) 
# XML ignores indentation and whitespace; indentation is included for readability.
# Nested tags are typically indented beyond their parent tree, to indicate the relationships.

<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>

# This XML can be accurately classified as having complex element "person", 
# ...simple elements "name" "phone", and "email", and attributes "type" and "hide"...
# ...the nodes in the above XML include "Chuck" and "+1 734 303 4456"

# Using ElementTree is a useful method in standardizing XML syntax:
# Code to parse elements from XML using ElementTree:

import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

# convert the string representation of XML into an "object tree" of XML nodes
tree = ET.fromstring(data)
# use find() function to retrieve a node matching an inputted tag 
print 'Name:',tree.find('name').text
# the get method added in will search for a specific attribute
print 'Attr:',tree.find('email').get('hide')

# If multiple nodes exist in a piece of XML, they can be looped through:

import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

# convert XML into a tree of nodes
stuff = ET.fromstring(input)
# retrieve a Python list of subtrees from the tree structure that represent the user structures in the XMLtree.
lst = stuff.findall('users/user')
print 'User count:', len(lst)

for item in lst:
    # print out a tag followed by its corresponding node
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get('x')
    
## JavaScript Object Notation (JSON)
# JavaScript's object and array format inspired the JSON format, but Python's syntax for dictionaries and lists...
# ... influenced the syntax of JSON, so JSON looks like a combination of Python lists and dictionaries.
# Generally, JSON structures are simpler and have less capabilities than XML.
# JSON maps directly to some combo of dictionaries and lists. JSON is natural because...
# ...nearly all programs have the equivalent of Python dictionaries/lists.
# In XML, attributes can be added to tags but in JSON, we simply have key-value pairs.
# In JSON, each element of the list corresponds to a user which itself contains dictionaries mapping keys to values for that user.
# Attributes do not exist in unique format as they do in XML, but are simply further key-value pairs.
# The outer tag included in XML is replaced in JSON with curly braces.
# JSON returns dictionaries that are easily parsable by subsetting a dictionary category (key) in order to return the corresponding value.
# JSON is frequently becoming the format of choice of data exchange between applications because of its relative simplicity. 

# JSON is constructed by nesting dictionaries and lists as needed.
# JSON has a built in JSON library (called JSON) to parse JSON and read through data.
# JSON has less detail but is also more succinct than XML.
# XML still finds use in areas such as word processing because its text is self-descriptive.

'''This JSON text shows the variable input as a list of dictionaries containing different users
whose data are being described by dictionaries '''

data = '''
    [
        { "id" : "001",
            "x" : "2",
            "name" : "Chuck"
        } ,
        { "id" : "009",
            "x" : "7",
            "name" : "Brent"
        }   
    ]'''


x =
"""   
{
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one .__.",
             },
             "location": "San Francisco, California",
             "screen_name": "leahculver",
             "name": "Leah Culver",
         },
        ...
        ]
}
"""

print(x["users"][0]["name"])    # returns "Leah Culver" by...
# ...subsetting the zeroth element of the "users" list, and finding the value ("Leah Culver") mapped from the "name" key


# Load JSON data into a variable containing list that can be parsed using standard Python list operations
info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']
    
## Application Programming Interfaces (API)
# "Contracts" stipulating the allowed sharing of data between applications are called Application Programming Interfaces (API).
# Generally, when an API is used, one program makes a set of services available for use by other applications...
# ...and publishes the API (or "rules") that must be followed to access the program's services.
# A Service-Oriented Architecture (SOA) approach is one where the application makes use of the services of other applications.
# A non-SOA approach is one where the application is a single standalone application which contains all necessary code.
# An SOA example occurs when the booking of multiple parts of a vacations are done on one website, by referring to different APIs at different booking stages.
# A Service-Oriented Architecture maintains only one copy of data and the owner can set rules about data usage.
# An application making a set of services in its API available over the web is a web service.

## Google geocoding web service.
# Google will show a map with a description of nearby landmarks when the respective location is inputted.

## Security and API Usage
# Oftentimes a vendor's API can only be accessed via referencing an "API key".
# API hits can be limited by usage fees and how many hits can be allowed in a time frame...
# ...x-rate-limit-remaining informs how many requests can be made before an API is shut off for a short time period.
# OAuth libraries are common APIs that can allow data to more easily be parsed.
# It is possible to parse Twitter data using the twurl library



