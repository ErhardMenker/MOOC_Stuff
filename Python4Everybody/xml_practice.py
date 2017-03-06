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
print ('User count:', len(lst))

for item in lst:
    # print out a tag followed by its corresponding node
    print ('Name', item.find('name').text)
    print ('Id', item.find('id').text)
    print ('Attribute', item.get('x'))