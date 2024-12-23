import os
try:
    os.remove("C:/Users/kj/.vscode/Python/demo.txt")
    if os:
        print("deleted")
except:
    print("Failed to Delete")


