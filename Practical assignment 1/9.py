f = open("names.txt", "r")
names = f.readlines()
f.close()

names = [name.strip() for name in names if name.strip()]

names = list(set(names))
names.sort(key=len)

f = open("processed_names.txt", "w")

for name in names:
    f.write(name + "\n")

f.close()

print("Processed names saved successfully")
