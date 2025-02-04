"""Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon,
 to return a part of the string."""
#######1
a="hello, world"
print(a[0:6])
#######2
#Slice From the Start
b="hello is the the python language"
print(b[:9])
#########3
#Slice To the End
c="hello i am creating a python syllabus"
print(c[2:])
#########4
#Negative Indexing
d="i am gonna upload it in github"
print(d[-6:-4])

#######5
#replacing values
e = "hello python"
print(e.replace("h","y"))