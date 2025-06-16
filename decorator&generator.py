#Function variable assignment

def hello():
    print("Hello!")

hello()
print(hello)
greet=hello
hello()
print(greet)
greet()
del hello
greet()
#hello()

# Function inside a function and "returns a function"

def hello1(name):
    print("Hello fn is executed!")

    def greet1():
        return("I am in greet()")
    
    def welcome1():
        return("I am in welcome()")
    
    print(greet1())
    print(welcome1())
    print("This is the end of hello1()")

    if name == 'Mahee':
        return greet1
    else:
        return welcome1

myvar=hello1('Mahee')
print(myvar)
print(myvar())


def cool():
    def super_cool():
        print("I am super cool!")

    return super_cool

func=cool()
print(func)
print(func())


# Passing Function as argument

def hello():
    return "Hello I am here"

def greet(some_func):
    print("Function is passed as argument")
    print(some_func())

print(hello)
print(hello())
print(greet)
print(greet(hello))


# Decorator

def new_decorator(func_name):
    def wrap_func():
        print("New code is decorated b4 old func")
        func_name()
        print("New code is decorated after old func")
    return wrap_func

@new_decorator
def func_decorate():
    print("Hi I need to be decorated")

# myfunc= new_decorator(func_decorate)
# print(myfunc())

print(func_decorate())


# Generators

def create_cube(num):
    for i in range(num):
        yield i**3                   # yield is the keyword used for generators.

print(create_cube(10))
print(list(create_cube(5)))


def fibonacci(num):
    a=1
    b=1
    #out=[]
    for i in range(num):
        #out.append(a)
        yield a
        a,b = b, a+b

print(list(fibonacci(7)))


#next keyword

def fun():
    for x in range(3):
        yield x

print(list(fun()))
f = fun()
print(f)
print(next(f))               # next() -> will remember the prev value and execute the next val. Hence Generators save space.
print(next(f))
print(next(f))

#iter function

s='Mahee'
s_inter = iter(s)           # Creating an iterate obj with the var
print(iter(s))          
print(next(s_inter))        # Using next() iterate thru the iter obj
print(next(s_inter))
print(next(s_inter))



#Problems - Q1

def gensquares(N):
    for i in range(N):
        yield i**2

for x in gensquares(10):
    print(x)
print(list(gensquares(10)))

#Q2

import random

def rand_num(low,high, n):
    for x in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)
print(list(rand_num(1,10,12)))


#Q3

s= 'hello'
s1_iter=iter(s)
print(next(s1_iter))
print(next(s1_iter))
print(next(s1_iter))

# Gencomp -> (x for x in [1,2,3,4,5] if x>3) -> o/p: 4  5 (Generator comprehension)
