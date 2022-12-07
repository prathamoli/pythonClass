studentsScore = [
    {
        'name':"Ram",
        "score":60
    },
    {
        'name':"Sita",
        "score":34
    },
    {
        'name':"John",
        "score":55
    },
    {
        'name':"Sita",
        "score":47
    },

    {
        'name':"John",
        "score":32
    },

    {
        'name':"Babita",
        "score":44
    },
]



print(list(filter(lambda n:n['score']>40,studentsScore)))

colors = ['yellow','red','green','blue','yellow','orange','red']
remove = ['yellow','red']



print(list(set(colors).difference(set(remove))))

newRemove= []

color1 = input('enter a color')
color2 = input('enter another color')

newRemove.append(color1)
newRemove.append(color2)

print(list(set(colors).difference(set(newRemove))))
