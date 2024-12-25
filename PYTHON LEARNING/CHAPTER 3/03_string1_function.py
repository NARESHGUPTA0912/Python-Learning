name = "harry"

print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))
print(name.capitalize())



# Some of the most commonly used string functions in Python include:

# len() - Returns the length of a string.
# lower() - Converts a string to lowercase.
# upper() - Converts a string to uppercase.
# strip() - Removes leading and trailing whitespace from a string.
# split() - Splits a string into a list of substrings based on a delimiter.
# join() - Joins a list of strings into a single string using a specified delimiter.
# replace() - Replaces occurrences of a substring within a string.
# find() - Returns the index of the first occurrence of a substring within a string.
# startswith() - Checks if a string starts with a specified prefix.
# endswith() - Checks if a string ends with a specified suffix.
# These string functions are frequently used for manipulating and working with textual data in Python programming.


text = "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello, world!"


text = "hello, world!"
upper_text = text.upper()
print(upper_text)  # Output: "HELLO, WORLD!"


text = "Hello, World!"
lower_text = text.lower()
print(lower_text)  # Output: "hello, world!"


text = "  Hello, World!  "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"


text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']


fruits = ['apple', 'banana', 'orange']
text = ", ".join(fruits)
print(text)  # Output: "apple, banana, orange"


text = "Hello, world!"
new_text = text.replace("world", "Python")
print(new_text)  # Output: "Hello, Python!"


text = "Hello, world!"
index = text.find("world")
print(index)  # Output: 7


text = "Hello, world!"
startswith_hello = text.startswith("Hello")
print(startswith_hello)  # Output: True


text = "Hello, world!"
endswith_world = text.endswith("world!")
print(endswith_world)  # Output: True