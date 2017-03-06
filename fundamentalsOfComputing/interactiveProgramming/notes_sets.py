# A set is an unordered collection of data with no duplicates.
# Sets are faster to process than lists, which are ordered and allow duplicates.
# Sets are created by declaring set() and storing a list within the parenthesis.
# In Python 3, sets can also be created by open curly braces, {}, and inputting elements within, separating by commas.
# By unordering, printing sets returns the elements in a seemingly random order.
# Trying to duplicate elements in set will simply eliminate the duplicates.
# Sets can be looped through.
# Calling the add.() method on sets adds additional inputted elements.
# Calling the remove.() method on sets removes the inputted element.
# Trying to remove something that is already in the set causes a KeyError.
# Therefore, conditional code can test to only remove an element if it exists in the set.
# Calling: s.intersection(t), where s and t are sets, returns the intersecting elements in these two sets,...
# ...but does not alter s nor t.
# Calling: s.intersection_update(t) updates set s as the intersection of it and t, but returns none when the method is printed.
# Generally, appending update to a set method will change the set being called, instead of creating a new set with that operation executed.

# Examples of Sets 

instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

inst2 = set(['Rixner', 'Rixner', 'Warren', 'Warren', 'Greiner', 'Wong'])
print inst2

print instructors == inst2

for inst in instructors:
    print inst

instructors.add('Colbert')
print instructors
instructors.add('Rixner')
print instructors

instructors.remove('Wong')
print instructors
#instructors.remove('Wong')
#print instructors

print 'Rixner' in instructors
print 'Wong' in instructors

# Examples of Sets 2:

instructors = set(['Rixner', 'Warren', 'Greiner', 'Wong'])
print instructors

def get_rid_of(inst_set, starting_letter):
    remove_set = set([])
    for inst in inst_set:
        if inst[0] == starting_letter:
            remove_set.add(inst)
    inst_set.difference_update(remove_set)

get_rid_of(instructors, 'W')
print instructors
