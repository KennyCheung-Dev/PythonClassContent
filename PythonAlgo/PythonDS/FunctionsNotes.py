'''

What is function?
Think of Function as a task

Use case:
Group codes
Repeat codes
Help with readability

Return
Python functions is loosely typed
you can return whatever data you like, or not return anything

Parameter
Parameters are inputs you take for your function to run
You can have as many input as you want, just have to declare you need them when you
write the function

Example 1
Function that returns an integer 1

def GiveMeOne():
    return 1

To use function value:
We can save it to a variable
x = GiveMeOne()
We can send it to console
print(GiveMeOne())

Common mistake:
Just leaving the function call without using the return
GiveMeOne()   <- nothing happened



Example 2
Function that returns nothing, but does something for you

def CoffeeSteps():
    MakeCoffee()
    PrepareCoffeeCup()
    DrinkCoffee()

To use function:
CoffeeSteps()

Common mistake:
Try to print a function that do not return:
print(MakeCoffee())  <= "None" appears on console



Example 3:
Function that takes a parameter

def MakeMultipleBubbleTea(number):
    for i in range(number):
        MakeBubbleTea()

To use function:
MakeMultipleBubbleTea(3)


Example 4:
Function that takes 3 parameters

def MakeMcdCombo(burger, drink, fries):
    MakeBurger(burger)'''

What is function?
Think of Function as a task

Use case:
Group codes
Repeat codes
Help with readability

Return
Python functions is loosely typed
you can return whatever data you like, or not return anything

Parameter
Parameters are inputs you take for your function to run
You can have as many input as you want, just have to declare you need them when you
write the function

Example 1
Function that returns an integer 1

def GiveMeOne():
    return 1

To use function value:
We can save it to a variable
x = GiveMeOne()
We can send it to console
print(GiveMeOne())

Common mistake:
Just leaving the function call without using the return
GiveMeOne()   <- nothing happened



Example 2
Function that returns nothing, but does something for you

def CoffeeSteps():
    MakeCoffee()
    PrepareCoffeeCup()
    DrinkCoffee()

To use function:
CoffeeSteps()

Common mistake:
Try to print a function that do not return:
print(MakeCoffee())  <= "None" appears on console



Example 3:
Function that takes a parameter

def MakeMultipleBubbleTea(number):
    for i in range(number):
        MakeBubbleTea()

To use function:
MakeMultipleBubbleTea(3)


Example 4:
Function that takes 3 parameters

def MakeMcdCombo(burger, drink, fries):
    MakeBurger(burger)
    MakeDrink(drink)
    MakeFries(fries)

To use function:

MakeMcdCombo("BigMac", "Coke", "Medium Fries")



Eample 5:
Function that takes parameter and return processed value

def MakeTriple(num):
    num = num * 3
    return num

OR

def MakeTriple(num):
    return num * 3

To use function:
tripledNumber = MakeTriple(300)

^ tripledNumber become 900


'''
    MakeDrink(drink)
    MakeFries(fries)

To use function:

MakeMcdCombo("BigMac", "Coke", "Medium Fries")



Eample 5:
Function that takes parameter and return processed value

def MakeTriple(num):
    num = num * 3
    return num

OR

def MakeTriple(num):
    return num * 3

To use function:
tripledNumber = MakeTriple(300)

^ tripledNumber become 900


'''