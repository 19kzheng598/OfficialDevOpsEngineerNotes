"""
                 | r   r+   w   w+   a   a+
------------------|--------------------------
read              | +   +        +        +
write             |     +    +   +    +   +
write after seek  |     +    +   +
create            |          +   +    +   +
truncate          |          +   +
position at start | +   +    +   +
position at end   |                   +   +
"""


"""Exception Handling


We need to create a program that allows users to create their own PIN codes for their bank cards. Each PIN code consists of digits. Complete the program so that when the user enters a character, the program stops and outputs "Please enter a number" and when the user enters only digits, the program outputs "PIN code is created".

Sample Input
44a5

Sample Output
Please enter a number"""
pin = input()
try:
    # your code goes here
    int(pin)
    print("PIN code is created")

except ValueError:
    # and here
    print("Please enter a number")


"""Exception Handling


A coffee vending machine makes 5 types of coffee:
coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"] 
PY
Each coffee option has its own number, starting with 0. Write a program that will take a number from the customer as input from the customer and serve the corresponding coffee type. If the customer enters a number that is out of the accepted range, the program should output "Invalid number". Regardless of coffee option result, the program should output "Have a good day" at the end.

Sample Input
7

Sample Output
Invalid number
Have a good day"""
coffee = ["Café Latte", "Caffe Americano",
          "Espresso", "Cappuccino", "Macchiato"]

choice = int(input())

try:
    # your code goes here
    print(coffee[choice])
except IndexError:
    # and here
    print("Invalid number")

finally:
    # and finally here
    print("Have a good day")


"""Reading files


Tom has done pull ups every day and recorded his results. He recorded each day's results in a new line, so that each line represents each day he has done pull ups.
Create a program that takes n number as input and outputs the n-th days result (starting from 0).

Sample Input
4

Sample Output
Day 4, 9 pull ups"""
file = open("/usercode/files/pull_ups.txt")
n = int(input())

# your code goes here
file_lines = file.readlines()
print(file_lines[n])

file.close()


"""Writing Files


You are given the following list:
names = ["John", "Oscar", "Jacob"] 
PY
Complete the program to create a file where you write the names from the list, each on a new line, and separately output them.

Output
John
Oscar
Jacob"""
names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")
# write down the names into the file
for i in names:
    file.write(i)

file.close()

file = open("names.txt", "r")
# output the content of file in console
sentence = file.readlines()
for i in sentence:
    print(i + "\n")

file.close()


"""Book Titles


You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Some book
Another book

Your program should output:
S9
A12"""
file = open("/usercode/files/books.txt", "r")

# your code goes here
lines = file.readlines()
lines_num = int(len(lines))

for i in range(0, lines_num):
    sentence = lines[i]
    if (i == lines_num - 1):
        print(sentence[0] + str(int(len(sentence))))
    else:
        print(sentence[0] + str(int(len(sentence) - 1)))


file.close()
