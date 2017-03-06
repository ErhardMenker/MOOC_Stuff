## Database Introduction
# A database is a file that is organized for storing data.
# Like dictionaries, most databases map keys to values.
# The first row of a database is typically metadata titling/describing the entry values that are listed below.
# Unlike dictionaries, databases live on disk instead of RAM, increasing storage capacity.
# Database software maintains performance by mapping indexes to its related entries.
# Common databases include Oracle, MySQL, Microsoft SQL Server, PostgreSQL, and SQLite.
# This course uses SQLite; it is very common and built into Python.
# SQLite is designed to be embedded into other applications to provide DB support from within.

## Database Concepts
# The primary data structures in a database are: table (relation), row (tuple), and column (attribute).
# Each tuple (row) title represents an object/concept, and respective entries present... 
# ...information about different charactristics of that object for each listed attribute.
# Each attribute (column) title lists a measure to be recorded for each tuple, and respective entries present...
# ...different values of that measure that correspond to the respective tuple.
# Tables map the different tuples (entries) to their respective attribute values.
# Database schema is a contract dictating how presented data should abstractly be structured.

## SQLite manager Firefox add-on
# Many SQLite operations can be done conveniently via the Firefox SQLite Database Manager.
# Simple DB edits can be done in the database manager, while more complicated ones can be done via Python.

## Creating a Database Table
# Databases require defined structure.
# A database administrator is responsible for the design, maintenance, and repair of an organization's database structure.
# A database table must know at time of creation the columns of the table and the type of data to be stored in each column.
# Defining data structure up front allows fast data access.
# Structured Query Language (SQL) is the standardized language in database-program interaction.
# As is convention, SQL keywords are expressed in uppercase while named parts of the command are lowercase.
# In Python, using sqlite requires calling: import sqlite3
# A cursor is used in analyzing DBs (like a file handle)
# The execute() method allows commands to be executed on DB content

import sqlite3

# make a "connection" to the DB stored in file 'music.sqlite3' in current directory (creates empty DB if none exists)
conn = sqlite3.connect('music.sqlite3')
# create cursor called 'cur' to current DB connection
cur = conn.cursor()
# drop Tracks table if it exists
cur.execute('DROP TABLE IF EXISTS TRACKS ')
# create Tracks table with text column title and integer column plays
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

conn.close()

# The SQL INSERT command inputs new data in a new row of the specified table...
# ...where new value entries are indicated by use of ? element tuples.

import sqlite3

conn = sqlite3.connect('music.sqlite3')
cur = conn.cursor()

# Into the Tracks table, insert two columns entitled title and plays...
# ...where the two inputted rows have the following actual values:
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?,?)', ('My Way', 15))
conn.commit()
print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
# loop through the rows of the DB by use of the cursor
for row in cur:
    print(row) # the preceding of these outputs with u' means that they are unicode, or...
               # ...capable of storing non-Latin characters

# delete entries from the DB where the Tracks entry is less than 100 (by use of conditional WHERE clause)
cur.execute('DELETE FROM Tracks WHERE plays < 100')
# force the data to be removed from the DB
conn.commit()
cur.close()

## Structured Query Language (SQL) Summary
# Relational databases store rows and columns of data in tables, and allow multi-table databases to be...
# ...mapped to each other in user designed ways by use of unique keys referenced across tables.
# Structure Query Language (SQL) is the standard interaction between the application level and the underlying machine level processing.
# SQL is very good with structured and prepped data, but Python is very good for doing the data prepping.
# The basic protocol of SQL is to create a table, retrieve date, insert the data, and then be prepared to delete data (CRUD).
# The names and types of the columns is stipulated at the time the table is created.

# Create a table called "Tracks" with "title" and "plays" columns of type "text" and "integer", respectively
CREATE TABLE Tracks (title TEXT, plays INTEGER)

# Insert a row with title entry 'My way' and plays entry 15
INSERT INTO Tracks (title, plays) VALUES ('My way', 15)

# The SQL SELECT command retrieves rows/columns from the DB, the WHERE allows for conditional selection,...
# ...and the ORDER BY clause can rank the output in ascending or descending alphabetical order.

# Return all columns of an instance where the observation title is 'My Way'
SELECT * FROM Tracks WHERE title = 'My Way'

# Logical operations in SQL match that in Python, except only one equal sign is needed to test equality (like EViews).

# SELECT takes a list of column (* implies all columns) from the database and returns them,... 
# ...WHERE allows for conditional code and ORDER BY orders alphabetically by the inputted column.

# Return title and plays from the Tracks database, but ordered alphabetically by the title
SELECT title,plays FROM Tracks ORDER BY title

# Delete from the Tracks table observations where title is 'My Way'
DELETE FROM Tracks WHERE title = 'My Way'

# Update the plays value to 16 where the corresponding title is 'My Way'
UPDATE Tracks SET plays = 16 WHERE title = 'My Way'

## Basic Data Modeling
# Because RAM dissapears when a program crashes but disk does not, it is often advisable to progressively write output out to disk in case of crashes.
# The real power of a relational database occurs when multiple tables are made with links between them.
# The act of deciding how to split data into multiple tables and determine the tables relationship is data modeling.
# The design document explaining the relationships and design of tables in a database is the data model.
# One of the primary rules in database normalization is to never put the same string data in the database more than once...
# ...instead, create a numeric key that uniquely maps a number to each possible string value. This saves computational power.
# These defining keys explaining a unique relationship must themselves occur uniquely in the database.
# This can be done by adding a UNIQUE clause, assuring that these input value combinations are indeed unique.
# Example of unique key SQL:
CREATE TABLE Follows (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id)) # from_id and to_id values can never each be the same in multiple entries
# Therefore, instead of repeating string data in the mother table, create another table for that column that maps each possible value to a primary key...
# ...and then put those primary keys in the main table as mother table foreign keys. 

## Constraints in Database Tables
# The IGNORE convention can allow for values to not be entered into the database if they would violate the UNIQUE condition.
cur.execute("INSERT OR IGNORE INTO People (name, retrieved) VALUES (?, 0)", (friend, )) # ignore insert attempt if uniqueness condition violated

## Three Kinds of Keys
# Similar rows linked through multiple tables are linked via keys.
# A logical key is a unique identifier of a row whose substance makes sense outside of the program (screenname).
# A primary key is a unique identifier key that makes no sense outside of the program, but computationally efficient, typically is a number (called an ID).
# Primary keys cannot be NULL.
# The autoincrement keyword can be used to make sure that primary key values are never repeated, even if original values were deleted.
# No ID needs to be specified when autoincrement is associated with it; the new number is generated automatically.
# A foreign key in a table refers to a primary key relationship that exists in another table in the database.
# By convention, primary and foreign keys are both positive integers.


## Using JOIN to retrieve data
# When rows in multiple tables share a common key, they may be merged via the JOIN clause.
# Using SELECT with JOIN calls on keys that must exist in all of the listed tables.
# The ON clause only matches where the equality between the stated one table's primary key matches the other table's foreign key.
SELECT * FROM FOllows JOIN People ON Follows.from_id = People.id # join all rows in the Follows and People table where the from_id equals the id key, in their respective tables.
# The JOIN creates extra-long "meta-rows" containing the unique fields of all the joined tables.
# JOIN two tables without an ON clause results in all possible combinations

## One-to-many and many-to-many relationships
# A one-to-many relationship maps multiple values to one characteristic (mapping many tracks to one and only one album).
# A many-to-many relationship maps multiple values to multiple characteristics (mapping authors to books, because...
# ...an author may write many books while a book may be written by multiple authors)
# Many-to-many relationships are typically modeled by having the main table be a junction "member" table that has as columns...
# ...foreign keys that map to the primary keys of other tables, so the non-identifying "member" entries should all be integers.
# However, when one entry has many relationships (such as one student mapping to multiple courses), then that student...
# ...is simply listed in the members table multiple times, so long as other defining characteristics vary (no two or more rows completely duplicate).
# Classifying unique combinations of a foreign key as a primary key in the junction table is called a "composite key."
# The uniqueness/primary-ness of the composite key is important because the many-to-many mapping that occurs at the junction...
# ...level should only occur one time, uniquely (a student should be mapped to a course at most once, if those two factors are all...
# ...that define this relationship).