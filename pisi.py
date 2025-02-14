f=open("text.txt", "a")
f.write("I added this text with f.write() method")
f.close()

print("I will now open the file again and read it with f.read() method")

f= open("text.txt", "r")
print(f.read())
f.close()

print("I will now make a new file and write some text in it")
f= open("newfile.txt", "w")
f.write("This is a new file")
f.close()