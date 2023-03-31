"""Lambdas


The given code takes a number as input and uses a lambda function to calculate its double and output the result.

Change the code to calculate the cube of the input and output it.

Sample Input
3

Sample Output
27"""
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
