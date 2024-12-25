friends = ["Apple", "Orange", "Aakash", 5, 345.45, False, "Rohan"]
print(friends)

friends.append("Harry")

print(friends)

li = [1,3,1 ,45, 23,87,11]
# li.sort()
# li.reverse()
# li.insert(3,3534) # insert 3534 such thst its index in the list is 3
print(li.pop(3))       # value = li.pop(3)
                        # print(value)
print(li)               


# Here is a list of common list methods in Python along with examples of each:

# append(): Adds an element to the end of the list.
# fruits = ['apple', 'banana', 'orange']
# fruits.append('grape')
# print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']


# insert(): Inserts an element at a specified position in the list.
# fruits = ['apple', 'banana', 'orange']
# fruits.insert(1, 'pear')
# print(fruits)  # Output: ['apple', 'pear', 'banana', 'orange']


# remove(): Removes the first occurrence of a specified element from the list.
# fruits = ['apple', 'banana', 'orange']
# fruits.remove('banana')
# print(fruits)  # Output: ['apple', 'orange']


# pop(): Removes and returns the element at a specified index in the list.
# fruits = ['apple', 'banana', 'orange']
# popped_fruit = fruits.pop(1)
# print(popped_fruit)  # Output: 'banana'
# print(fruits)  # Output: ['apple', 'orange']


# index(): Returns the index of the first occurrence of a specified element in the list.
# fruits = ['apple', 'banana', 'orange']
# index = fruits.index('orange')
# print(index)  # Output: 2


# count(): Returns the number of times a specified element appears in the list.
# fruits = ['apple', 'banana', 'orange', 'apple']
# count = fruits.count('apple')
# print(count)  # Output: 2


# sort(): Sorts the elements of the list in ascending order.
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.sort()
# print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]


# reverse(): Reverses the order of the elements in the list.
# fruits = ['apple', 'banana', 'orange']
# fruits.reverse()
# print(fruits)  # Output: ['orange', 'banana', 'apple']


# extend(): Extends the list by appending elements from another iterable.
# fruits = ['apple', 'banana']
# more_fruits = ['orange', 'grape']
# fruits.extend(more_fruits)
# print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']


# clear(): Removes all elements from the list.
# fruits = ['apple', 'banana', 'orange']
# fruits.clear()
# print(fruits)  # Output: []
