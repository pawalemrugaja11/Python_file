f = open("names.txt", "r")
names = f.readlines()
f.close()

frequency = {}

for name in names:
    name = name.strip()

    if name:
        name = name.lower()
        frequency[name] = frequency.get(name, 0) + 1

print(frequency)
