f = open("names.txt", "r")
names = f.readlines()
f.close()

for name in names:
    name = name.strip()

    if name:
        print("Name:", name)
        print("Length:", len(name))
        print("First character:", name[0])
        print("Last character:", name[-1])

        if name.lower() == name[::-1].lower():
            print("Palindrome: Yes")
        else:
            print("Palindrome: No")

        print()
