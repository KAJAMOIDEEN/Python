try:
    f = open("C:/Users/kj/.vscode/Python/demo.txt","r")
    if f:
        print(f.readline())
    f.close
except:
    print("Failed to Read")


