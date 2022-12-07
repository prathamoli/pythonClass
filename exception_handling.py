try:
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
except ValueError:
    print("cannot convert to decimal")
else:
    print(a+b)

name = input("Enter the name")
print(name)
