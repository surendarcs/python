'''User Input
Python allows for user input.
That means we are able to ask the user for input.
The method is a bit different in Python 3.6 than Python 2.7.
Python 3.6 uses the input() method.
Python 2.7 uses the raw_input() method.
The following example asks for the username, and when you entered the username, it gets printed on the screen:'''
############1
name = input("enter name: ")
print("name is " + name)
###########2
username = raw_input("Enter username:")
print("Username is: " + username)
