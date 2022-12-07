a = []
for i in range(2,20,2):
    a.append(i)
print(a)

b = [i for i in range(2,30,2)]
print(b)

emails = ["1@gmail.com","1@gmail.com","1@gmail.com","1@yahoo.com","1@yahoo.com"]

gmail = [i for i in emails if i.endswith("gmail.com")]

print(gmail)
