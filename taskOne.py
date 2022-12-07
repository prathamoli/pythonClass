name = input("Enter the student name: ")
classNo = (input("enter student class: "))
rollNo = (input("enter student rollNo: "))
marksOne = int(input("enter marks one: "))
marksTwo = int(input("enter marks two: "))
marksThree = int(input("enter marks three: "))

total = marksOne + marksTwo + marksThree
percentage = total/3

print(" Student Name : " + name)
print(" Student class : " + classNo)
print(" Student rollNo : " + rollNo)
print(" marks 1 : " + str(marksOne))
print(" marks 2 : " + str(marksTwo))
print(" marks 3 : " + str(marksThree))
print(" total : " + str(total))
print(" percentage : " + str(percentage) + " %")

if percentage < 40:
    print("You have failed")
else:
    print("You have passed your examination")
