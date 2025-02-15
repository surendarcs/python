'''F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
Before Python 3.6 we had to use the format() method.

F-Strings
F-string allows you to format selected parts of a string.
To specify a string as an f-string, simply put an f in front of the string literal, like this:'''
########1
txt = f"The price is 49 dollars"
print(txt)
#########2
'''Placeholders and Modifiers
To format values in an f-string, add placeholders {}, a placeholder
can contain variables, operations, functions, and modifiers to format 
the value.'''
price = 59
txt = f"The price is {price} dollars"
print(txt)
#######3
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)
