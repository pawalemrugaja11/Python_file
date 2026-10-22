f = open("names.txt", "r")
names = f.readlines()
f.close()

for name in names:
    name = name.strip()
    if len(name) > 5:
        print(name)
