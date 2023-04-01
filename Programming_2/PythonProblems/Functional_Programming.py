"""Lambdas


The given code takes a number as input and uses a lambda function to calculate its double and output the result.

Change the code to calculate the cube of the input and output it.

Sample Input
3

Sample Output
27"""
from itertools import permutations
x = int(input())
print((lambda z: z**3)(x))


"""filter


Given a list of names, output a list that contains only the names that consist of more than 5 characters."""
names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

# your code goes here
print(list(filter(lambda x: len(x) > 5, names)))


"""Generators


Given a string as input, create a generator function that splits the string into separate words and outputs the resulting list.

Sample Input
This is some text

Sample Output
['This', 'is', 'some', 'text']"""
txt = input()


def words():
    # your code goes here
    for word in txt.split():
        yield word


print(list(words()))


"""Decorators


You are given code that takes input and prints it as a simple row of text.

Add the uppercase_decorator to make the text uppercase."""
text = input()


def uppercase_decorator(func):
    def wrapper(text):
        # your code goes here
        return (text.upper())
    return wrapper


@uppercase_decorator
def display_text(text):
    return (text)


print(display_text(text))


"""Recursion


The provided code uses recursion to calculate the sum of all items in the input list.

Change the code to calculate and output the sum of the squares of all the list items."""


def calc(list):
    if len(list) == 0:
        return 0
    else:
        return list[0]**2 + calc(list[1:])


list = [1, 3, 4, 2, 5]
x = calc(list)
print(x)


"""Sets

The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.
x.add() adds an item to the set
x.remove() removes a item from the set
x.pop() removes a arbitrary element

Sets are created using curly braces and they hold unique values.

Given two sets, find and output all the elements that are common to both sets.
For example, for the following sets:
{'a', 'b', 'c'}
{'c', 'd', 'e'}

The output should be {'c'}, as it is present in both sets."""
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8, 11, 42, 2}

# your code goes here
print(set1 & set2)


"""
takewhile - takes items from an iterable while a predicate function remains true;
chain - combines several iterables into one long one;
accumulate - returns a running total of values in an iterable.
The function count counts up infinitely from a value.
The function cycle infinitely iterates through an iterable (for instance a list or string).
The function repeat repeats an object, either infinitely or a specific number of times.
There are also several combinatoric functions in itertool, such as product and permutation.
REMEMBER, always type cast to a list at the end.

itertools


You are given a list of items, and need to find all the possible orders of the items.
The output should be a list, containing all possible orders.

Sample Input
['a', 'b']

Sample Output
[('a', 'b'), ('b', 'a')]
"""

items = ['x', 'y']

# your code goes here
print(list(permutations(items)))


"""Fibonacci


The Fibonacci sequence is one of the most famous formulas in mathematics.
Each number in the sequence is the sum of the two numbers that precede it.
For example, here is the Fibonacci sequence for 10 numbers, starting from 0: 0,1,1,2,3,5,8,13,21,34.

Write a program to take N (variable num in code template) positive numbers as input, and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).

Sample Input
6

Sample Output
0
1
1
2
3
5"""
num = int(input())


def fibonacci(n):
    # complete the recursive function
    # append adds to the end of a list
    nth_list = [0, 1]
    i = 0
    while n > 2:
        n -= 1
        nth_list.append(nth_list[i] + nth_list[i+1])
        i += 1
    return nth_list


fibonacci_list = fibonacci(num)

for i in fibonacci_list:
    print(i)
