import os

print("I will now delete the new file")

if(os.path.exists("newfile.txt")):
    os.remove("newfile.txt")            
else:
    print("The file does not exist")


