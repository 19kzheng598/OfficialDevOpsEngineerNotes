"""Dictionaries


Dictionaries can be used to store key:value pairs.

You have been asked to create an inventory management program for a store. You use a dictionary to track all of the store's inventory along with how many of each item the store has.
store = {"Orange": 2, "Watermelon": 0, "Apple": 8, "Banana": 42} 
PY
Complete the provided code to output the number of apples present in the store."""
import math
store = {"Orange": 2, "Watermelon": 0, "Apple": 8, "Banana": 42}

# your code goes here
print(store["Apple"])


"""Dictionary Functions


You can use the .get() method to find keys in a dictionary, and use a second parameter to return a default value, in case the key is not found.

Rewrite the given code to use the .get() method instead of the if/else statements.
Also, change the output to "Book not found", when the book is not found."""
books = {
    "Life of Pi": "Adventure Fiction",
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics",
    "Bird Box": "Horror",
    "Harry Potter": "Fantasy Fiction",
    "Good Omens": "Comedy"
}

book = input()

# change this part to use the .get() method
print(books.get(book, "Book not found"))


"""Tuples


You are given coordinates of 2 points and need to find the straight line distance between them.

The coordinates are provided in a tuple, for example:
p = (8, 11) 
PY
The first value represents the x coordinate, while the second value represents the y coordinate of the point p.

Complete the provided code to calculate and output the distance between the two given points."""

p1 = (23, -88)
p2 = (6, 42)

# your code goes here
print(math.sqrt((23 - 6)**2 + (-88 - 42)**2))


"""
List Slices


Write a program that takes a list as input and outputs the last element of that list.

The input list can be of any size.
"""
x = input()
elements = x.split()

# your code goes here
print(elements[-1])


"""List Comprehensions


Write a program to take a number as input, and output a list of all the numbers below that number, that are a multiple of both, 3 and 5.

Sample Input
42

Sample Output
[0, 15, 30]"""
x = int(input())
# your code goes here
print([i for i in range(0, x+1) if i % 5 == 0 and i % 3 == 0])


"""String Formatting


The .format() method provides an easy way to format strings.
Take as input a name and an age, and generate the output "name is age years old".

Sample Input
James
42

Sample Output
James is 42 years old"""
name = input()
age = int(input())

# your code goes here
print("{0} is {1} years old" .format(name, age))


"""Useful Functions


Your friend sent you a message, however his keyboard is broken and types a # instead of a space.

Replace all of the # characters with spaces and output the result."""
txt = input()

# your code goes here
print(txt .replace("#", " "))


"""Word Counter


Given text as input, output the number of words it contains.

Sample Input
hello world

Sample Output
2"""
txt = input()

# your code goes here
print(len(txt .split(" ")))


"""Longest Word


Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome"""
txt = input()

# your code goes here
length = 0
# print nothing if there is no words
word = ""
txt = txt.replace(",", "")
txt_list = txt.split(" ")

for new_word in txt_list:
    if len(word) <= len(new_word):
        word = new_word

print(word)


# Useful functions
print(", ".join(["spam", "eggs", "ham"]))
# prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
# prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
# prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
# prints "['spam', 'eggs', 'ham']"
