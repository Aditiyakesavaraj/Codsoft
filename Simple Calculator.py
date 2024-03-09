def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print("Please select operation - \n"
      "1.Add \n"
      "2.Sub \n"
      "3.Multiply \n"
      "4.Divide \n")
choose = int(input("Select operations form 1, 2, 3, 4 : "))
num1 = int(input("Enter a First Number : "))
num2 = int(input("Enter a Second Number : "))
if choose == 1:
    print(num1, " + ", num2, " = ", add(num1, num2))
elif choose == 2:
    print(num1, " - ", num2, " = ", sub(num1, num2))
elif choose == 3:
    print(num1, " * ", num2, " = ", multiply(num1, num2))
elif choose == 4:
    print(num1, " / ", num2, " = ", divide(num1, num2))
else:
    print("Invalid Input")