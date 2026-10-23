f = open("names.txt", "r")
names = f.readlines()
f.close()

for name in names:
    name = name.strip()
    if "a" in name.lower():
        print(name)
