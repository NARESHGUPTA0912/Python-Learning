s = {8, 7, 12, "Prince", [1,2]}

# No,, you cannot change the value inside a list contained in a set in pythonin fact, you cannot even have a list as an element in a 
# set because sets in python require all their elements to be immutable and hashable. Lists are mutable and not hashable, so they
# cannot be added to a set.

# if u try to create  a set with a list as one of its element, python will raise a 'TypeError' .