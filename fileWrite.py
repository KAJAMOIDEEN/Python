try:
    f = open("C:/Users/kj/.vscode/Python/demo.txt","wt")
    f.write("Hi This is my first Python File")
    f.close
    if f:
        print("Written in the file")
except:
    print("Failed to wi=rite")


