""" NOTE: VERY IMPORTANT SCRIPT; SAME CONTENT AS CHAP_14_HW.PY FILE """

import xml.etree.ElementTree as ET
import sqlite3

# Make a connection to trackdb.sqlite in the current folder
conn = sqlite3.connect('trackdb.sqlite')
# Create cursor to this database called "cur"
cur = conn.cursor()

# Make some fresh tables using executescript()
# Create Artist, Album, Track, Genre tables after dropping them if they existed
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# SAMPLE XML:
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
# Parse every XML entry containing three nested dictionaries using ElementTree
for entry in all:
    # if "Track ID" entry is NoneType, go to next iteration
    if ( lookup(entry, 'Track ID') is None ) : continue
    
    # else extract the attributes of the Track
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')
    
    # if any of these elements are none, abort this iteration
    if name is None or artist is None or album is None or genre is None: 
        continue

    print(name, artist, album, count, rating, length, genre)

    # insert into each table the relevant attributes, remembering that autoincrement...
    # ...takes care of the primary key assignment (insert does not occur if entry already occurred for that value).
    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    # extract the zeroth element of this entry, which is the id (used for input into Track mother table to assure equality)
    genre_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
    
    # Input all of the proper keys extracted from each block above in the Track mother table.
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()
