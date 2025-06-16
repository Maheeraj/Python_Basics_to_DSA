# try, except, else  ----> try-pass; except-no execution; else-get executed. / try-fail; except-execution; else-no execution



try:
    result=10+10
except:
    print("This block will be executed only if try block gets an error")
else:
    print("try worked without error and hence else works")
    print(result)


# try, except, finally   ---> try-pass; except-no execution; finally-get executed. / try-fail; except-execution; finally-get execution
    
try:
    f=open('testfile','r' )
    f.write("Write a test line")
# except TypeError:
#     print("There was a type error")
# except OSError:
#     print("Hey u have an OS error")
except:
    print("all other exceptions")
finally:
    print("I always run")


# try, except, else, finally inside a method


# while True:
#     try:
#         num = int(input("Please provide a number: "))
#     except:
#         print("Oops, It's not a number")
#         continue
#     else:
#         print(f"You have entered : {num}")
#         break
#     finally:
#         print("I will be executed all the time")


#Problem - Q1
        
try:
    for i in ['a','b','c'] :
        print(i**2)
except:
    print("Variables can't be squared")

#Q2

try:
    x=5
    y=0
    z=x/y
except:
    print("Value becomes undetermined")
finally:
    print("All DOne")

#Q3


def ask():
    while True:
        try:
            num = int(input("Enter a num: "))
            val=num**2
        except:
            print("Oops, pls eneter a number!")
            continue
        else:
            print(f"The square is {val}")
            break

ask()



