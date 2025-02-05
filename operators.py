'''Python Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:'''
#########1
print(10+15) #addition
x =5
y=6
print(x-y)  #substraction
print(x+y)  #addition
print(100+15*3) #addition and substraction

######### logical operators
####AND OR NOT
#1 AND
a = 5
print(a>3 and a<9)
##########OR
#2 OR
b=5
print(b>3 or b<4) ## returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
##########NOT
#3 NOT
c=5
print(not(c>3 and c<10))
# returns False because not is used to reverse the result
