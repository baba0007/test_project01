# module name conflict:
# incase of same member name in a module , the last one will be the winner

def add(a, b):
    print('modul1 add function:')
    print('Sum =', a + b)


# will return list of members of the current module modul1.py and also will return other members python default.
print(dir())
