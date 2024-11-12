thisdict = {
    "c10" : "the secret",
    "d10" : "the space",
    "d13" : "dr.ambedkar",
    "j9": "the pain",
    "j8": "the pain"
}



print(thisdict.get("j9"))

thisdict["k9"] = "the sucesss"

# for x in thisdict:
#     print(thisdict.get(x))

for x,y in thisdict.items():
    print(x,y)