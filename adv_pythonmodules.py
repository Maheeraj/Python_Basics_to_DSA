# Collections module

#counter

from collections import Counter

l=[1,1,1,12,2,2,3,3,4,4,4,4,4,4]
print(Counter(l))

s='asdafjsadbfjbsdjfbsdjfbjsadfc'
print(Counter(s))

st= 'Mahee Mahee Mahee is is a a a a good boy boy' 
st_list=st.split()
print(Counter(st_list))


c= Counter(st_list)
print(len(c))
print(c.most_common(2))
print(sum(c.values()))
print(list(c))



# defaultdict

from collections import defaultdict

d= {'k1':1}
print(d['k1'])

d = defaultdict(object)
print(d['one'])
for i in d:
    print(i)

d= defaultdict(lambda: 0)
print(d['ones'])
d['two']=2
for i in d.items():
    print(i)

# Ordered Dict
    
from collections import OrderedDict

d= OrderedDict()
d['a']=1
d['b']=2
d['c']=3
d['d']=4

for k,v in d.items():
    print (k,v)

d1= {}
d1['a']=1
d1['b']=2

d2= {}
d2['b']=2
d2['a']=1

if d1==d2:
    print ("True, normal dict does not be ordered")

d1= OrderedDict()
d1['a']=1
d1['b']=2

d2= OrderedDict()
d2['b']=2
d2['a']=1

if d1==d2:
    print ("True, normal dict does not be ordered")
else:
    print('False, Now I am in Ordered dict. Values are not ordered equally')


#namedtuple
    
from collections import namedtuple

Dog= namedtuple('Dog','age breed name')
sam = Dog(age=5, breed='Lab', name='Sammy')
print(sam.age)
print(sam[1])

Cat = namedtuple('Cat','fur claws name')
kit=Cat(fur='fizzy', claws=False, name='Kitty')
print(kit.claws)
print(kit[0])

# Datetime

import datetime

print(datetime.time(5,25,1))
t=datetime.time(5,25,1)
print(t.hour)
print(t.second)
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)


today = datetime.date.today()
print(today)
print(today.year)
print(today.timetuple())
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)

d1= datetime.date(2025,2,27)
print(d1)
d2= d1.replace(year=2002)
print(d2)

print(d1-d2)


# Python Debuggr

import pdb

x=[1,2,3]
y=2
z=3

result=y+z
print(result)

#pdb.set_trace()     ---> It creates an interactive debugging envirnomnet, where we can check what is the error is.
result1=y+z
print(result1)


# timeit module

import timeit

print(timeit.timeit('"-".join([str(n) for n in range(100)] ) ', number=10000))
print(timeit.timeit('"-".join(map(str,range(100))) ', number=10000))
#print(%timeit "-".join(map(str,range(100))))


# Regular expressions

import re

patterns =['term1','term2']

text = 'This is a string with term1, but not the other term'

for pattern in patterns:
    print(f"Searching for {pattern} :")

    if re.search(pattern, text):
        print("\nMatch FOund")
    else:
        print("\nMatch not found.")

matche = re.search(pattern[0],text)

print(type(matche))
print(matche.start())
print(matche.end())

split_term= '@'

phrase = "WHat is your email, is it hello@gmail.com?"

print(re.split(split_term, phrase))

print(re.findall('match','Here is one match, another match'))


# Repetition set & Character sets - refer jupyter NB

# exclusion

text = 'Hi I am  string! am i good?'
print(re.findall('[^!.? ]+', text))

# character changes

# Escape codes

# StringIO

# import StringIO

# msg='Hi this is mahee'

# f = StringIO.StringIO(msg)

# print(f.read())