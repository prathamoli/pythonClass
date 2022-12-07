heroes = ["spider man","thor","hulk","iron man","captain america"]

print(len(heroes))
heroes.append("black panther")
print(heroes)

for i in range(len(heroes)):

    if heroes[i] == "black panther":
        heroes.remove("black panther")
        print(heroes)


for i in range(len(heroes)):

    if heroes[i] == "hulk":
        heroes.insert(i+1,"black panther")
        print(heroes)
        break



heroes[1:3] = ["dr strange"]
print(heroes)

heroes.sort()

print(heroes)



a= [8,10,7,4,3,4]
a[0]
a[-1]
# a [start:stop:step]
# a[2:5]





