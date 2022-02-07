def add(a, b):
    return a + b


print(__name__)
if __name__ == '__main__': # is used when we import this file to another file it wont let this result of this file to be returned in the other file
    print(add(5, 15))
