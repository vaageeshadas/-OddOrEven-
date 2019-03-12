inputNum = input("Enter an integer: \n")

#Check if enter value is proper
try:
    savedNum = int(inputNum)
except ValueError:
    print("That's not proper!")
    quit()


if savedNum == 2:
    print("That's 2!")
elif savedNum == 5:
    print("That's 5, you silly!")
elif savedNum % 2 == 1:
    print("Odd")
else:
    print("Even")
