# one.py -----> Compare with two.py for __name__ and __main__

def func():
    print("Im func() in ONE.py")

print(" 0 indentation msg in ONE.py")

if __name__=='__main__':
    print("one.py is being run directly")
else:
    print("one.py is being imported!")