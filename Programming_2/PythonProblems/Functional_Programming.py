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
