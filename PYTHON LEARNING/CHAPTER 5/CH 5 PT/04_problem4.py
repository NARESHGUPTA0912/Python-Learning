s = set()
s.add(20)
s.add(20.0)
s.add("20") # what is the length of s after these operations ?

print(len(s))

# ans : length is 2 
# because in python, 1 == 1.0 