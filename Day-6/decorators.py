#Nested Functions - A function defined inside another function is called a nested function. Nested functions can access variables of the enclosing scope.

def outer(x):
    def inner(y):
        return x + y
    return inner

temp = outer(10)

print(temp(20))


#Pass Function as Argument - we can pass a function as an argument to another function.

def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)

print(result)

#python decorators - A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty	#decorator
def ordinary():
    print("I am ordinary")

decorated_func = make_pretty(ordinary)

decorated_func()


#@ symbol is used to decorate a function with another function. It is just a short way of calling the decorator function.

#create a decorator check_positive that, 
# 1. check if the input to a function is a postive number
    # if the input is not positive, print a message "input must be a positive number"
# 2. use this decorator on a function, calculate_squareroot
    # takes one number as input
    # return the square root of the number

def check_positive(func):
    def inner(x):
        if x <= 0:
            print("input must be a positive number")
        else:
            return func(x)
        
    return inner

@check_positive
def calculate_squareroot(x):
    return x ** 0.5

decorated_func = calculate_squareroot(25)
print(decorated_func)

decorated_func = calculate_squareroot(-25)
print(decorated_func)

