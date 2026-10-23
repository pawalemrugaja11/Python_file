f = open("names.txt", "r")
names = f.readlines()
f.close()

names = [name.strip() for name in names]
names.sort()

print(names)
