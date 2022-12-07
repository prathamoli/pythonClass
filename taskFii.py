email = [
    'oli.pratham56@gmail.com','beats@gmail.com','dad@gmail.com','cat@gmail.com','eh@yahoo.com'
]

out = filter(lambda name:name.endswith('@gmail.com'),email)

print(list(out))
######


a = '457d89e36'

b = list(a)

but = filter(lambda b:b.isdigit(),b)
hu = map(lambda b:int(b),but)

print(sum(hu))


cv = '12d57d54d90'
e = cv.split('d')
jj= map(lambda c:int(c),e)
print(sum(jj))

#define a function which returns a list of prime numbers between provided range

def getPrime(a,b):
    for i in range(a,b+1):
        num = i
        flag=False
        if num > 1:
            for v in range(2, num):
                if (num % v) == 0:
                    flag = True
                    break

        if flag == False:
            print(num)

getPrime(1,100)
