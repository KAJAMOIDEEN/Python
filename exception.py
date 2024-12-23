try:
    res = 9
    print(res)
except ZeroDivisionError:
    print("division by zero")
except NameError:
    print("Variable res is not defined")
finally:
    sum = 9 * 8
    print(sum)
if sum>550:
    raise Exception("Amount is greater than 50")    



