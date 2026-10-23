f = open("names.txt", "r")
names = f.readlines()
f.close()

f = open("filtered_names.txt", "w")

for name in names:
    name = name.strip()
    if len(name) > 5:
        f.write(name + "\n")

f.close()

print("Filtered names saved successfully")
