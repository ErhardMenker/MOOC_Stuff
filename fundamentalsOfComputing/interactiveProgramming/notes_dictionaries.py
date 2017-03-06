# Python dictionaries map unique keys to values.
# Dictionaries are created with curly braces and have keys and values separated by a colon.
# Individual key-value pairs are separated by commas.
dict = {1:2, 3:4, 6:727}
# Value elements can be any type of characters, while keys must be numbers or strings.
# Dictionaries can be iterated over, and will loop through the dict's keys in an arbitrary appearing order...
# ...this defaulted behavior can be specified by tacking on .values() to the end of the dictionary.
# Tacking on .items() to the end of the iterated dictionary means that key-pairs are being iterated over...
# ...so two iterated variables will be used, where the first maps to the iterated key and the second to the iterated value.
# Tacking on .values() to the end of the dictionary iterates through the values of the key-value pairs.
# Unlike lists, dictionaries are not ordered and trying to subset in similar ways looks for keys matching the subsetted value
# Dictionaries are mutable, and so setting an existing key value (using list subset notation) to a new value changes the value that key is mapped to
# If an added key-value pair calls a key that does not exist for a dictionary, it is simply created.

# Cipher

import simplegui

CIPHER = {'a': 'x', 'b': 'c', 'c': 'r', 'd': 'm', 'e': 'l'}

message = ""

# Encode button
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print message, "encodes to", emsg

# Decode button
def decode():
    dmsg = ""
    for ch in message:
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print message, "decodes to", dmsg

# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode)

# Start the frame animation
frame.start()
