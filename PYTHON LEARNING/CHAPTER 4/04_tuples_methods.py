# Certainly! In Python, tuples are ordered collections of elements, similar to lists, but they are immutable, meaning their contents cannot be changed after creation. Here are some common methods and operations you can perform with tuples:

# Creating Tuples
# python
# Copy code
# # Creating a tuple
# tup = (1, 2, 3, 4, 5)
# Accessing Elements
# python
# Copy code
# # Accessing elements in a tuple
# print(tup[0])  # Output: 1
# print(tup[2:4])  # Output: (3, 4)
# Tuple Methods
# count(): Counts the number of occurrences of a specified value in the tuple.

# python
# Copy code
# tup = (1, 2, 2, 3, 4, 2)
# print(tup.count(2))  # Output: 3 (2 appears 3 times in the tuple)
# index(): Returns the index of the first occurrence of a specified value.

# python
# Copy code
# tup = ('a', 'b', 'c', 'a', 'd')
# print(tup.index('a'))  # Output: 0 (index of the first 'a')
# Other Operations
# Concatenation
# python
# Copy code
# tup1 = (1, 2, 3)
# tup2 = (4, 5, 6)
# tup3 = tup1 + tup2
# print(tup3)  # Output: (1, 2, 3, 4, 5, 6)
# Membership Test
# python
# Copy code
# tup = ('a', 'b', 'c')
# print('b' in tup)  # Output: True
# print('d' in tup)  # Output: False
# Iteration
# python
# Copy code
# tup = ('apple', 'banana', 'cherry')
# for item in tup:
#     print(item)
# # Output:
# # apple
# # banana
# # cherry
# Immutable Nature
# python
# Copy code
# tup = (1, 2, 3)
# # Trying to modify a tuple will result in an error:
# # tup[0] = 4  # TypeError: 'tuple' object does not support item assignment
# Tuples are particularly useful when you want to store a collection of items that should not be changed, such as coordinates, settings, or other immutable data sets.



