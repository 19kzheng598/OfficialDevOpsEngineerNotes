"""Functions


We have a function that outputs "Welcome, user" as it is called. We want to make it more personalized, so redesign the given function so that it will take the given input as the name of the user and output the welcome message with it.

Sample Input
Tommy

Sample Output
Welcome, Tommy"""


import random


def welcome_message():
    # redesign this function
    name = input()
    print("Welcome, " + name)


welcome_message()


"""Function Arguments


You are given a program with two inputs: one as password and the second one as password repeat. Complete and call the given function to output "Correct" if password and repeat are equal, and output "Wrong", if they are not.

Sample Input
nfs1598
nfs1598

Sample Output
Correct"""
password = input()
repeat = input()


def validate(text1, text2):
    # your code goes here
    if (text1 == text2):
        print("Correct")
    else:
        print("Wrong")


validate(password, repeat)


"""Returning from Functions


We are creating our own social network application and need to have a hashtag generator program.
Complete the program to output the input text starting with the hashtag (#).
Also, if the user entered several words, the program should delete the spaces between them.

Sample Input
code sleep eat repeat

Sample Output
#codesleepeatrepeat

Hint
You can use the replace() function to replace the spaces (" ") with empty strings (""). See how it works:
s = "I like pears"
s1 = s.replace("pears", "apricots")
print(s1)

#prints I like apricots"""
s = input()


def hashtagGen(text):
    # your code goes here
    text_no_space = text.replace(" ", "")
    return "#" + text_no_space


print(hashtagGen(s))


"""Modules


Two friends want to play backgammon, but have lost the dice.
Create a program to replace the dice. When the program is run, it should roll the dice and output the result of each die.

Hint
Use random.randint() function to generate random values in the range of 1 to 6 for each dice."""
random.seed(int(input()))  # please don't touch this lane

# generate the random values for every dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print(dice1)
print(dice2)


"""Celsius to Fahrenheit


You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

Sample Input
36

Sample Output
96.8"""
celsius = int(input())


def conv(c):
    # your code goes here
    return c * (9/5) + 32


fahrenheit = conv(celsius)
print(fahrenheit)
