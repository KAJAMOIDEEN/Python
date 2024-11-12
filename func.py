def sum():
    print("This is Sum Function...")

sum()


def sum(a,b):
    c = 5
    sum = a+b+c
    return sum

def sumof4(a,b,c,d):
    return a+b+c+d


def empty():
    pass


def arbitrary(*param):
    print("Mutliple Parameter:",param[1])

arbitrary("first","second","third")

def arbitraryObj(**param):
    print("Mutliple Parameter:",param["second"])

arbitraryObj(first="first",second="second",third="third")

print("Sum is",sum(9,8))
print("Sum of 4 number:",sumof4(90,89,90,809))

    