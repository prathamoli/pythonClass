main = []
odd = []
even = []
duplicate = []



for i in range(0,15):

    num = int(input("enter a number"))

    if num in main :
        duplicate.append(num)
    else:
        if num % 2 ==0:
            even.append(num)
        else:
            odd.append(num)

    main.append(num)


print(main,odd,even,duplicate)

