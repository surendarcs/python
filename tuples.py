'''Tuple
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.'''
######1 basic syntax
tuple = ("apple","banana","orange")
print(tuple)
#######2 access tuple
tuple2 = ("apple","banana","orange")
print(tuple2[2])
#######3 Join Two Tuples To join two or more tuples you can use the + operator:
tuple5 = ("a","b","c")
tuple6 = (1,2,3)
tuple7 = tuple5 + tuple6
print(tuple7)
