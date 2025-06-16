#Class attributes and methods

class Car():
    wheels = "Four"                     # CLASS OBJECT Attribute; we need not mention as self.wheel because it is common for all the instances.
    def __init__(self,cartype, color, brand, year, new):        # __init__ -> constuctor ; self -> it is an instance we can use it as a reference inside the class
        self.cartype = cartype
        self.color = color                                     # color, brand,... -> attributes
        self.brand = brand
        self.year = year
        self.new = new

    def throttle(self, speed):                                       # Method -> Method is a function which is present inside the class.
        print(f"{self.color} {self.brand} is throttled at {speed} kmph with {self.wheels} wheels")       # self.wheels -> Class Object attribute needs to be addressed with self inside methods or we can also call as Car.wheels (class_name.attribute_name) -> only for Object class attribute

mycar = Car(cartype="SUV", color="Blue", brand="Benz", year=2025, new=True)     #mycar -> Instance of the class.
print(type(mycar))
print(mycar.brand)
print(mycar.color)
print(mycar.wheels)
print(mycar.throttle(60))


# Inheritance

class Animal():                                 # Base Class
    def __init__(self):
        print("Animal(BASE) Class created")

    def eat(self):
        print("I am eating")

    def who_am_i(self):
        print("I am an animal")

class Tiger(Animal):                             # Derived Class
    def __init__(self):
        Animal.__init__(self)
        print("Tiger(DERIVED) class created")

    def who_am_i(self):                          #Method is overrided in the derived class
        print("I am a Tiger")

    def hunt(self):
        print("Yes, I will hunt")

myanimal=Animal()                              # Base class methods
print(myanimal)
myanimal.who_am_i()
myanimal.eat()

mytiger= Tiger()                               # Derived class methods
print(mytiger)
mytiger.who_am_i()
mytiger.eat()                                 # Dervied class instance can use the methods in Base class
mytiger.hunt()


# Polymorphisim

class Animal():                              # Base class -> In this case, used only for getting the name.
    def __init__(self, name):
        self.name = name
        print("Animal created")

    def speak(self):
        raise NotImplementedError("Subclass must implement the abstract method")
    
class Dog(Animal):                          # Derived class 1
    def speak(self):
        return self.name + " says Woof!"
    
class Cat(Animal):                           # Derived class 2
    def speak(self):
        return self.name + " says meow!"
    
mycat=Cat("Poonai")
mydog = Dog("Naai")

print(mycat.speak())
print(mydog.speak())


#Special Methods

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):                                 # whenever we use print(obj_name) we will get only the loc. add. , but by using this method, we can return some value.
        return f"{self.title} by {self.author}"
    
    def __len__(self):                                  # if we use normally, it will throw error, but by using this method, we can avoid and return value.
        return self.pages
    
    def __del__(self):
        print( "Class objected is deleted!")
    
mybook=Book('Kavidhai','Maheeraj',60)
print(mybook)
print(len(mybook))
del(mybook)
#print(mybook)  -> Now, we can't print it, because obj is deleted.


#PROBLEMS

#Q1

class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return ((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)**0.5
    
    def slope(self):
        return ((self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0]))

co1=(3,2)
co2=(8,10)

li= Line(co1,co2)
print(li.distance())
print(li.slope())

#Q2

class Cylinder():
    pi = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi*self.height*(self.radius**2)
    
    def surface_area(self):
        return (2*self.pi*self.radius*self.height)+(2*self.pi*(self.radius**2))


c= Cylinder(2,3)
print(c.volume())
print(c.surface_area())

# Challengs pblms - Q3

class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"
    
    def deposit(self, val):
        self.balance += val
        print(f"Deposit Accepted. Your balance is - {self.balance}")

    def withdraw(self, val):
        if self.balance < val:
            print ("Funds Unavailable!!!")
        else:
            self.balance-=val
            print(f"WIthdrawl Accepted. Your balance is - {self.balance}")

acct= Account('Mahee',100)
print(acct)
print(acct.owner)
print(acct.balance)
acct.deposit(50)
acct.withdraw(75)
acct.withdraw(500)
print(acct)
            


        
