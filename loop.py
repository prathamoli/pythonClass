x = sum(range(1,101))
print(x)


total = 0
for i in range(1,101):
    if i%3==0 or i%5==0:
        total+=i

print(total)

three = sum(range(3,101,3))
five = sum(range(5,101,5))
fiveteen = sum(range(15,101,15))
print(three+five-fiveteen)


for i in range(1,10):
    if i % 7 == 0 :
        continue
    print(i)
