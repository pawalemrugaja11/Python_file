f = open("demo.txt", "r")
data = f.read()
words = data.split()
d = {}

for word in words:
    d[word] = d.get(word, 0) + 1

print(d)
f.close()
