total = lambda a,b:a+b
print(total(10,20))

def increment_by_one(n):
    return n+1

a = [1,2,3,4,5]

b = map(increment_by_one,a)

print(
    list(b)
)

c = map(lambda n:n+2,a)

print(
    list(c)
)

names = ['ram','shyam','gita','babita','sabita']

d = map(lambda name:name.capitalize(),names)
print(list(d))

x = [1,2,4,5,6,7,8]

def is_even(num):
    return num % 2 == 0

out = filter(lambda n:n % 2 == 0,x)
print(list(out))

