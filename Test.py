print("Hello World")
print(type(123))

#Variable declaration & type()
var = 5
print(var+var)
print(type(var))
var=10.5
print(type(var))

a=5
b=10
c=a*b
print(c)

ma=['mahee']
print(ma)
print(type(ma))

#Strings

test="Maheeraj"
print(test)
print(len(test))
print(len("Kee"))
print(test[0])
print(test[4])
print(test[-1])
print(test[0:5])
print(test[2:])
print(test[2:7])
print(test[2:-1])
print(test[::2])
print(test[2:7:2])
print(test[::-1])       # Reverse the string

#len()
z=(1,2,3)
y={'a':'b','c':'d'}
x=[1,2,3,4]
print(len(z))
print(len(y))
print(len(x))


 #Concatenation

m="Sem"
n=m[1:]
m= 'Po' + n     # string concatenation
print(m)

print(m*10)   # string multiplication

#Methods

x="Hello"
print(x)
print(x.upper())
print(x.lower())
x="Hello World Mahee"
print(x.split())
print(x.split('e'))

#Print Formatting
#.format() method

print("Hi {}".format('Mahee'))
print("Hi {}".format(x))
print("Hi {} {}".format('Mahee','Raj'))
print("Hi {1} {0}".format('Mahee','Raj'))

#float formatting methods

r=100/777
print(r)
print("The result is {re}".format(re=r))
print("The result is {re:1.3f}".format(re=r))    #x.yf --- x-> width(white space) ; y-> precision (decimal digits)


#f-string method
name='Mahee'
age=22
print(f"My name is {name} , {age} years old.")


#Lists

my_list=[1,'Mahee',['a','b'],2.5]
print(len(my_list))
print(my_list[1:])
an_list=my_list[1:3]
print(an_list)
print(my_list + an_list)
print(my_list)
my_list[0]=20
print(my_list)
my_list.append('50')       #append operation
print(my_list)
my_list.append('7')       
print(my_list)
popped=my_list.pop()      #pop operation   for specific item to pop, pop(0)  --- 0 is index position
print(popped)
print(my_list)
alpha_list=['b','x','a','y']
num_list=['4','1','2','3']
alpha_list.sort()                    #sort operation
num_list.sort()
print(alpha_list)
print(num_list)
num_list.reverse()                       #reverse operation
print(num_list)



#Dictionaries - {'key':value}

my_dict={'k1':'a','k2':2,'k3':[1,2,3,'a','b'],'k4':{'a':1}}
print(my_dict)
print(my_dict['k3'])
print(my_dict['k4']['a'])
print(my_dict['k3'][2])
print(my_dict['k3'][3].upper())
my_dict['k3'][2]=100
print(my_dict)
my_dict['k5']=5.55
print(my_dict)
print(my_dict.keys())
print(my_dict.items())
print(my_dict.values())


#Tuples

t=(1,2,3,'a',(1,2))
print(type(t))
print(len(t))
print(t[2])
print(t[-1])
t1=('a','a','a','b')
print(t1.count('a'))
print(t1.index('b'))

#Sets

s=[1,1,1,'a','b','a',2,2,1]
my_set=set()
my_set.add(1)
my_set.add(2)
print(my_set)
print(set(s))

#Booleans

print(type(True))
print(1>2)             #Comparison operators
print(1==1)              #Comparison operators
b=None
print(b)

#Files

my_file= open("abc.txt")
print(my_file.read())
print(my_file.read())     # Empty string as o/p, since cursor went to last.
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.readlines())
my_file.close()

with open ('D:\\Python programs\\abc.txt', mode='a') as my_new_file:        # It appends in the file
     my_new_file.write('\nGoood boyyy')

with open ('D:\\Python programs\\def.txt', mode='w') as my_new_file1:       # It will overwrite if file exists, if not it will create one and write.
     my_new_file1.write('\nMaheeraj')



# Logical and Comparison operators
     
print(1<2 and 2>3)
print(1<2 or 2>3)
print('h' == 'h' and 2 == 2)
print(not(1==1))

#Control statement (if,elif,else)

hungry = False
if hungry:
     print('FEED ME!')
else:
     print("I'm full")

loc="Bank"
if loc == "Auto":
    print("Cars are cool")
elif loc == "Bank":
     print("Money is cool")
else:
    print("Don't know")


#For loops

mylist= [1,2,3,4,5,6,7,8]
for num in mylist:
    print(num)
    if num%2 == 0:
        print(f'{num} is Even ')
    else:
        print('Odd')

sum=0
for a in mylist:
    sum = sum + a
print(sum)

for letter in "Maheeraj":
    print(letter)

name1="Willson"
for letter1 in name1:
    print(letter1)

tup=(1,2,3)
for b in tup:
    print(b)

mylist=[(1,2),(3,4),(5,6)]
print(len(mylist))
for c in mylist:
    print(c)
for a,b in mylist:           #Tuple unpacking
    print(a)
    print(b)

mydict={'k1':1,'k2':2,'k3':"Mahee"}
for a in mydict:
    print(a)

for a in mydict.items():
    print(a)

for a in mydict.values():
    print(a)   



#while loops
    
x=0
while x<5:
    print(x)
    x+=1
else:
    print("x exceeds 5")

#break,continue,pass
    
y=[1,2,3]
for a in y:
    pass
print("No error faced")

stri="Sammy"
for lett in stri:
    if lett=="a":
        continue
    print(lett)

stri="Sammy"
for lett in stri:
    if lett=="m":
        break
    print(lett)

x=0
while x<5:
    if x==3:
        break
    print(x)
    x+=1

#Useful Operators
    
for num in range(1,4):     #range operator -> range(start,stop,index)
    print(num)

index=0
for index,letter in enumerate("abcde"):              #enumerate operator
    print(f" the {index} letter is {letter}")

mylist=[1,2,3]
mylist1=['a','b','c']
for item in zip(mylist,mylist1):                 #zip operator --> Zip till only the shortest length.
    print(item)

print(list(zip(mylist,mylist1)))


print(2 in [1,2,3])                      # in operator
print('a' in "Mahee")
d={'k1':123}
print(123 in d.values())


mylist=[10,20,30,100]
print(min(mylist))                       #min operator
print(max(mylist))                      #max operator

from random import shuffle            #Random operator
shuffle(mylist)
print(mylist)


from random import randint
print(randint(0,100))


# o = input('Enter number:')              #Input function --- Always it takes input value as string.
# print(o)

# o = int(input('Enter number:'))
# print(o)


#List comprehensions
word="Mahee"
mylist=[letter for letter in word]
print(mylist)

mylist=[x**2 for x in range(4)]
print(mylist)

mylist=[x+10 for x in range(11) if x%2==0]
print(mylist)










     