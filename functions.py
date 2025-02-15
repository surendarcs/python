'''A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.'''
##############1  CREATING A FUNCTION  --------- syntax
def my_function():
    print("hello from a function")
my_function()   #######you need to call a function
'''Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:'''
#################2
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#############3
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
############4
'''Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:'''
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
