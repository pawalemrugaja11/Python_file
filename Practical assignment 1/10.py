f = open("names.txt", "r")
names = f.readlines()
f.close()
groups = {}

for name in names:
    name = name.strip()

    if name:
        letter = name[0].upper()

        if letter not in groups:
            groups[letter] = []

        groups[letter].append(name)

for letter, group in groups.items():
    filename = letter + "_names.txt"

    f = open(filename, "w")

    for name in group:
        f.write(name + "\n")

    f.close()

print("Names grouped into separate files successfully")
