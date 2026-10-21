f1 = open("demo.txt", "r")
lines = f1.readlines()
f1.close()

f2 = open("even.txt", "w")

for i in range(len(lines)):
    if (i + 1) % 2 == 0:
        f2.write(lines[i])

f2.close()
print("Even-numbered lines copied")
