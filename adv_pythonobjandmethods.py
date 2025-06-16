#Advanced numbers
#Hexadecimal number
print(hex(512))

#Binary number
print(bin(64)) 

# power functon
print(pow(2,3))

#absolute function
print(abs(-2))
print(abs(3))

#round function
print(round(3.2))
print(round(4.8))
print(round(3.14267,2))

#Advanced Strings

s='mahee raj'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.count('e'))
print(s.find('r'))
print(s.center(13,'z'))
print("hello\thi")

s='hello'
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isupper())
print(s.isspace())
print('Hello'.istitle())
print('HELLO'.isupper())
print(s.endswith('o'))
print(s.split('e'))
print(s.partition('l'))


# Advanced Sets

s=set()
s.add(1)
s.add(2)
print(s)

s.clear()
print(s)
s={1,2,3}
sc = s.copy()
print(sc)
s.add(4)
print(s)
print(s.difference(sc))

s1={1,2,3}
s2={1,4,5}
print(s1.difference_update(s2))
print(s1)
print(s)
s.discard(2)
print(s)

s1={1,2,3}
s2={1,2,4}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)

s1={1,2}
s2={1,2,4}
s3={5}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s1.symmetric_difference(s2))
print(s1.union(s2))
print(s1.update(s2))
print(s1)

# Advanced Dictionaries

d= {'k1':1,'k2':2}
print({x:x**2 for x in range(10)})
print({k:v**2 for k,v in zip(['a','b'], range(2))})

# Advanced Lists

l=[1,2,3,4]
l.append(5)
print(l)
print(l.count(4))

x=[1,2,3]
x.append([6,7])
print(x)
x.extend([4,5])
print(x)

print(l.index(3))
print(l.insert(1,'inserted'))
print(l)
l.pop()
print(l)
l.pop(1)
print(l)
l.append(1)
l.append(1)
print(l)
l.remove(1)
print(l)
l.reverse()
print(l)
l.sort()
print(l)


#Problems - Q1

print(bin(1024))
print(hex(1024))

#Q2

print(round(5.23222,2))

#Q3

s="hello how are you Mary, are you feeling okay?"
print(s.islower())

#Q4

s='twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

#Q5

s1={2,3,1,5,6,8}
s2={3,1,7,5,6,8}

print(s1.difference(s2))

#Q6

print(s1.union(s2))

#Q7

print({x:x**3 for x in range(5)})

#Q8

l=[1,2,3,4]
l.reverse()
print(l)

#Q9

l=[3,4,2,5,1]
l.sort()
print(l)

