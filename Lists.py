'''List
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store
collections of data, the other 3 are Tuple, Set, and Dictionary,
 all with different qualities and usage.'''
#######1  basic lists syntax
mylist = ["apple","banana","orange"]
print(mylist)
#######2 List Length To determine how many items a list has, use the len() function:
thelist = ["apple","banana","orange"]
print(len(thelist))
######3 type of list
thislist = ["apple","banana","orange"]
print(type(thislist))
#####4  accessing list item
list = ["apple","banana","orange","kiwi", "mango","pineapple"]
print(list[1])
print(list[:5])
print(list[2:])
print(list[0:])
print(list[-1:])
print(list[-3])
#####5 Change List Items
list1 = ["apple","banana","orange","kiwi", "mango","pineapple"]
list1[1] = "blackcurrant"
print(list1)
list1[1:3] = ["chocklate", "lemon"]
print(list1)
######6 Add List Items
######To add an item to the end of the list, use the append() method
list2 = ["apple","banana","orange","kiwi", "mango","pineapple"]
list2.append("lemenon")
print(list2)
######7 Remove List Items
###### The remove() method removes the specified item.
list3 = ["apple","banana","orange","kiwi", "mango","pineapplle"]
list3.remove("apple")
print(list3)
######8 Sort Lists
###### List objects have a sort() method that will sort the list alphanumerically, ascending, by default.
list4 = ["apple","banana","orange","kiwi", "mango","pineapplle"]
list4.sort()
print(list4)
######9 Join Two Lists
#There are several ways to join, or concatenate, two or more lists in Python.
#One of the easiest ways are by using the + operator.
list5 = ["a","b","c"]
list7 = [1,2,3]
list6 = list5 + list7
print(list6)