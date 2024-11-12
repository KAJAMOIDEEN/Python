thislist = ["apple","apple", "banana", "cherry"]
# print(thislist)
# print(thislist[1])
# thislist[1] = "blackcurrant"
# print(thislist)

# for x in thislist:
#     print(x)


if "apple" in thislist:
    print("Yes")
else:
    print("no")


newlist = thislist.copy()

print(newlist)