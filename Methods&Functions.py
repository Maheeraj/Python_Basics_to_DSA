mylist=['1','2','3']
my="".join(mylist)       # We need to use split() to split the whole string to list of strings ; Similarly use .join() to make a single string out of list of strings.
print(my)

#Functions

def name_fn(name):
    return "Hello " + name

var=name_fn("Mahee")
print(var)


def addd(n1,n2):
    return n1+n2

res=addd(5,4)
print(res)

def dog_check(mystring):
    return 'dog' in mystring.lower()

print(dog_check("Dog is good"))


# PIG LATIN

def pig_latin(mystring):
    if mystring[0] not in "aeiou":
        temp= mystring[1:] + mystring[0] + 'ay'
    else:
        temp = mystring + 'ay'
    return temp

print(pig_latin("word"))
print(pig_latin("apple"))

#args,  kwargs

def myfunc(*args):                        #it will take i/p as tuple but can take multiple i/p's. (*args- 'args'is user defined)
    print(args)
    return sum(args) * 0.05

print(myfunc(1,2,3,4))

def myfunc1(**kwargs):                        #key-value pair, similar to args.[**jelly, also works.]
    if 'fruit' in kwargs:
        print(f"The fruit is {kwargs['fruit']}")
    else:
        print("No fruit")
    

mydict={'k1':'a','fruit':'apple'}
print(myfunc1(fruit='apple',veggie='tomato'))
print(myfunc1(veggie='tomato'))

def myfunc(*args, **kwargs):                                   # args and kwargs together
    print(args)
    print(kwargs)
    return(f"I would like {args[0]} and {kwargs['food']}")

print(myfunc(10,20,30, fruit="apple", food="Mutton"))

#Function Practice pblms

#Q1

def lesser_of_two_evens(a,b):
    if a%2 ==0 and b%2 ==0:
        return min(a,b)
    else:
        return max(a,b)
    
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(7,5))

#Q2

def animal_crackers(text):
    mylist=text.split()
    print(mylist)
    if mylist[0][0].lower() == mylist[1][0].lower():
        return True
    else:
        return False
    
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

#Q3

# def other_side_of_seven(num):
#     temp= num*2
#     temp1=21-temp
#     return temp1

# print(other_side_of_seven(4))
# print(other_side_of_seven(12))

def makes_twenty(n1,n2):
    return n1 == 20 or n2 == 20 or (n1+n2) == 20

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))



#Level 1 - Q4
def old_macdonalod(name):
    # first_word= name[:3]
    # second_word= name[3:]
    # return first_word.captialize() + second_word.captialize()

    temp=name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return temp


print(old_macdonalod("macdonald"))

#Q5

def master_yoda(text):
    mylist=text.split()
    mylist.reverse()
    mylist1= " ".join(mylist)
    return mylist1

print(master_yoda("I am home"))
print(master_yoda("We are ready"))

#Q6

def almost_there(num):
    # if (num >= 90 and num <= 110) or (num >= 190 and num <= 210):
    #     return True
    # else:
    #     return False
    print("Q6")
    return (abs(100-num) <= 10) or (abs(200-num)<=10)
    
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

#Level 2 pblm - Q7

def has_33(nums):
    # index=1
    # flag= False
    # for temp in nums:
    #     if index < len(nums):
    #         if temp == 3 and nums[index] == 3  :
    #             flag= True
    #             break
    #         else:
    #             flag=False
    #         index+=1
    # return flag
    for i in range(0, len(nums)-1):
        if nums[i] ==3 and nums[i+1]==3:
            return True
    return False

print("Q7")
print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))


#Q8

def paper_doll(text):
    word=''
    for i in text:
        word += i*3
    return word


print(paper_doll('Hello'))
print(paper_doll('Mahee'))

#Q9

def blackjack(a,b,c):
    val=a+b+c
    if val > 21 and 11 in [a,b,c]:
        val -= 10
    if val <= 21:
        return val
    else:
        return "BUST"
    
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print(blackjack(11,11,11))

#Q10

def summer_69(arr):
    val=0
    flag= True
    for i in arr:
        if i==6:
            flag= False
        if flag:
            val+=i
        if i==9:
            flag= True
    return val

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))


# Challenging Pblms - Q11

def spy_game(arr):
    code=[0,0,7,'x']
    for i in arr:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


#Q12

def prime_num(num):
    prime_cnt=0
    cnt=0
    mylist=[]
    if num < 2:
        return 0
    for i in range(2, num+1):
        for j in range (1, i+1):
            if i%j == 0:
                cnt+=1
        if cnt ==2:
            mylist.append(i)
            prime_cnt+=1
        cnt=0
    print(mylist)
    return prime_cnt

print(prime_num(100))

    
# Map function

def square(num):
    return num**2

mylist=[2,3,4,5]
for i in map(square, mylist):
    print(i)


def splicer(str):
    if len(str)%2==0:
        return "EVEN"
    else:
        return str[0]
    
name=['Maheee','Mahee','Raj']
print(list(map(splicer, name)))


#Filter function

def check_even(num):
    return num%2==0

mynum=[1,2,3,4,5,6]
print(list(filter(check_even, mynum)))           # filter(func, var) --- only filters depending on Boolean value, and only filters True.

#Lambda expression

square1 = lambda num : num**2
print(square1(9))

print(list(map(lambda num:num**3, mynum)))
print(list(filter(lambda num:num%2==0, mynum)))
print(list(map(lambda name: name[::-1], name)))


# Nested statements and Scope --- LEGB RUle

x=25

def printer():
    x=50
    return x

print(x)
print(printer())


name='Mahee Global'        #Global variable

def greet():
    #name="Willy"           #Enclosing variable
    def hello():
        #name = "Raj"              #Local variable
        print ('Hello ' + name)
    hello()

greet()



# Questions
#Q1

def vol(rad):
    return (4/3)*(3.14)*(rad**3)

print(vol(5))

#Q2

def ran_check(num, low, high):
    return num in range(low, high+1)

print(ran_check(4,1,10))
print(ran_check(14,1,10))

#Q3

def up_low(s):
    up_count=0
    small_count=0
    for i in s:
        if i.isupper():
            up_count+=1
        elif i.islower():
            small_count+=1
    return (up_count, small_count)

print(up_low("Hello Mr. Rogers, how are you this fine Tuesday?"))

#Q4

def unique_list(l):
    return list(set(l))

print(unique_list([1,1,1,2,2,2,3,3,4,4,5,5,5]))

#Q5

def multiply(num):
    mul=1
    for i in num:
        mul*=i
    return mul

print(multiply([1,2,3,-4]))

#Q6

def palindrome(stri):
    return stri == stri[::-1]

print(palindrome('helleh'))

#Q7

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset= set(alphabet)
    #print(string.ascii_lowercase)
    #print(alphaset)
    #print(set(str1.lower()))
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))












            
    






