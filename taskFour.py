a = int(input("number 1 :"))
b = int(input("number 2 :"))
c = int(input("number 3 :"))

if a >= b and a >= c:
    print("number 1 is the greatest number ",a)
elif b >= a and b >= c:
    print("number 2 is the greatest number ",b)

else:
     print("number 3 is the greatest number ",c)
