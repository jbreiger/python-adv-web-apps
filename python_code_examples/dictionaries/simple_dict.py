"""explore a simple Python dictionary"""

import pprint
pp = pprint.PrettyPrinter(indent=4)

# below is a Python dictionary - note how it differs in structure from
# a Python list - a dictionary stores key-value PAIRS
cat = { 'eyes': 'green',
    'fur': 'brown',
    'name': 'Furball',
    'nose': 'pink',
    'tail': 'short' }

# ADD a NEW item to the dictionary
cat.update( {'ears':'pointy'} )

# CHANGE an item in the dictionary - same as adding a new item
cat.update( {'fur':'orange'} )

print() # blank line

print(cat)

print() # blank line

# we imported pprint (not normally needed for dictionaries)
# just so we could see this difference in printing in Terminal
pp.pprint(cat)

print() # blank line

print('Print the value of "nose":')
print(cat['nose'])

print() # blank line

print('Print the value of "name":')
print(cat['name'])

print() # blank line

print("The cat's name is " + cat['name'] + " and the cat's nose is " + cat['nose'] + ".")

print() # blank line

new_name = input("Give the cat a new name: ")

cat.update( {'name':new_name} )

print("The cat's name is now " + cat['name'] + ".")

print() # blank line
