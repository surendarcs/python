'''What is an Array?
An array is a special variable, which can hold more than one value at a time.
If you have a list of items (a list of car names, for example), storing the cars in single variables'''
######1
cars = ["bmw","benz","audi"]
print(cars)
'''Access the Elements of an Array
You refer to an array element by referring to the index number.'''
######2
cars = ["bmw","benz","audi"]
x = cars[0]
print(x)
########3 Modify the value of the first array item:
cars = ["bmw","benz","audi"]
cars[0] = "toyato"
print(cars)
########4 The Length of an Array-----------Use the len() method to return the length of an array (the number of elements in an array).
cars = ["bmw","benz","audi"]
x = len(cars)
print(x)
'''Looping Array Elements
You can use the for in loop to loop through all the elements of an array.'''
########5
cars = ["bmw","benz","audi"]
for x in cars:
    print(x)

'''Adding Array Elements
You can use the append() method to add an element to an array.'''
##########6
cars = ["bmw","benz","audi"]
cars.append("honda")
print(cars)

'''Removing Array Elements
You can use the pop() method to remove an element from the array.'''
########7
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
########8
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)

