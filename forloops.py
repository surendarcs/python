'''Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''
#########1
fruits = ["apple","mango","orange"]
for x in fruits:
    print(x)
#########2
for x in "banana":
    print(x)
#########3
#The break Statement --------With the break statement we can stop the loop before it has looped through all the items.
fruit=["lemeon","grapes","pineapple","watermelon"]
for x in fruit:
    print(x)
    if x=="pineapple":
        break 
##########4
###The continue Statement-----------With the continue statement we can stop the current iteration of the loop, and continue with the next
fruits1 = ["apple", "banana", "cherry"]
for x in fruits1:
  if x == "banana":
    continue
  print(x) 
##########5
##### The range() Function  To loop through a set of code a specified number of times,
# we can use the range() function, The range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x) 
##############
for x in range(2, 6):
  print(x) 
##############
for x in range(2, 30, 3):
  print(x) 
####   Else in For Loop    The else keyword in a for loop specifies a block of code to be executed when the loop is finished