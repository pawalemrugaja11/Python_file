f1 = open("demo.txt", "r")
data = f1.read()
f1.close()

f2 = open("copy.txt", "w")
f2.write(data)
f2.close()

print("File copied successfully")
