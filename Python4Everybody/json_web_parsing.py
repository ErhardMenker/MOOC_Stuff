import urllib
import json

# This is the main website where data will be parsed:
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

# Once one university Place ID is parsed, another input can be entered in the command...
# ...line (note that entering an empty string will break from the loop)
while True:
    address = input('Enter location: ')
    if len(address) < 1: 
        break
    # Concatenate user inputted address to above URL:
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print('Retrieving', url)
    # Use urrlib open to access URL and...
    uh = urllib.urlopen(url)
    # ...enact the read() method on that URL variable and...
    data = uh.read()
    print("Length of read in is: ", len(data))
    # ...use the JSON load string method to view the JSON in readable form
    js = json.loads(str(data))
    # Go to the zeroeth element in the results list of the JSON, and extract the value mapped from the "place_id" index in the dictionary list element
    print("Place ID is :", js["results"][0]["place_id"])
    
    # Below commented code prints out JSON to command line, useful in determining...
    # ...parsing logic based on what you are trying to get from parsing the JSON:
    print(json.dumps(js, indent=4))
    
    
    

    

