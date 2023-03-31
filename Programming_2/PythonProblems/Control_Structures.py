"""if Statements


Write a program that checks if the water is boiling.
Take the integer temperature in Celsius as input and output "Boiling" if the temperature is above or equal to 100.

Sample Input
105

Sample Output
Boiling"""
temp = int(input())
# your code goes here
if temp >= 100:
    print("Boiling")


"""else Statement


Write a program to control entrance to a club.
Only people who are 18 or older are allowed to enter the club.
The given program takes the age and the name of the person who tries to enter. Complete the program to output "Welcome" followed by the name of the person if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.

Sample Input
24
James

Sample Output
Welcome James"""
age = int(input())
name = input()
# your code goes here
if age >= 18:
    print("Welcome " + name)
else:
    print("Sorry")


"""
Boolean Logic


The comfortable relative humidity for humans is between 40% and 60%.
The given program takes the percent of humidity as input.

Task
Complete the code to output "norm" if the taken percent of humidity is in the range of 40 and 60 inclusive.
Don't output anything otherwise.

Sample Input
45

Sample Output
norm"""
humidity = int(input())
# your code goes here
# hint: humidity
if humidity >= 40 and humidity <= 60:
    print("norm")


"""
Chaining Multiple Conditions


Using an ATM, customers can access their bank deposits or credit accounts to do a variety of financial transactions.
You serve ATMs that accept only Visa and Amex bank cards.
The given program takes the type of a bank card as input.

Task
Complete the program to output "accepted" if the card is Visa or Amex.
Don't output anything otherwise.

Sample Input
Amex

Sample Output
accepted"""
type = input()
# your code goes here
if type == "Visa" or type == "Amex":
    print("accepted")


"""Lists


Imagine a vending machine that sells fruits. Each fruit has its own number, starting from 0.
Write a program for the vending machine, which will take n number as input from the customer and return the fruit with that index.
fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"] 
PY
If n< 0 or n>7 (the index of last fruit ), the program outputs "Wrong number".

Sample Input:
2

Sample Output:
banana"""
fruits = ["apple", "cherry", "banana", "kiwi",
          "lemon", "pear", "peach", "avocado"]
num = int(input())
# your code goes here
if num >= 0 and num <= 7:
    print(fruits[num])
else:
    print("Wrong number")


"""List Operations


Given a list of numbers, output "bingo" if it contains the input number."""
items = [42, 88, 721, 12, 43, 22, 908]

num = int(input())
# your code goes here
if num in items:
    print("bingo")


"""List Functions


Given a list, calculate the middle element's index."""
items = [2, 4, 6, 8, 10, 12, 14]

# your code goes here
print(len(items)//2)


"""while Loops


You have a magic box that doubles the count of items you put, in every day.
The given program takes the initial count of the items and the number of days as input.

Task
Write a program to calculate and output items' count on the last day.

Sample Input
3
2

Sample Output
12

Explanation
Day 1: 6 (3*2)
Day 2: 12 (6*2)"""
items = int(input())
days = int(input())
# your code goes here
while (days > 0):
    days -= 1
    items *= 2

print(items)


"""for Loops


for loops allow you to easily iterate through lists.

Given a list of numbers, output their sum.

Sample Input
1 3 7 5

Sample Output
16"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
# your code goes here
for add in list:
    sum += add

print(sum)


"""Range


You are making a date picker for a website and need to output all the years in a given period.
Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.
The output sequence should start with the first input number and end with the second input number, without including it.

Sample Input
2005
2011

Sample Output
[2005, 2006, 2007, 2008, 2009, 2010]"""
a = int(input())
b = int(input())
# your code goes here
Years = list(range(a, b))
print(Years)


"""FizzBuzz


FizzBuzz is a well known programming assignment, asked during interviews.

The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers which are multiples of both 3 and 5, output "SoloLearn".

You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range."""
n = int(input())

for x in range(1, n):
    if (x % 2 == 0):
        continue
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)