f1 = open("demo.txt", "r")
data1 = f1.read()
f1.close()

f2 = open("copy.txt", "r")
data2 = f2.read()
f2.close()

if data1 == data2:
    print("Files are identical")
else:
    print("Files are not identical")
