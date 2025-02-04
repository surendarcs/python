'''Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.'''

#Create a variable outside of a function, and use it inside the function
x="awesome"
def myfunc():
    print("python is " + x)
myfunc()

'''If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function.
 The global variable with the same name will remain as it was, global and 
 with the original value.'''

x="awesome"
def myfunc():
    x='fantastic'
    print("python is " + x)
myfunc()
print('python is ' + x)

'''The global Keyword
Normally, when you create a variable inside a function, that variable is local,
and can only be used inside that function.
To create a global variable inside a function, you can 
use the global keyword.'''
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

############--------
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
