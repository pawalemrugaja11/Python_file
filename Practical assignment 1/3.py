f = open("names.txt", "r")
names = f.readlines()
f.close()

count = 0

for name in names:
    name = name.strip()
    if name and name[0].lower() in "aeiou":
        count += 1

print("Count:", count)
