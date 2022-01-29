num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
num3 = input("Enter a number: ")
num4 = input("Enter a number: ")
num5 = input("Enter a number: ")
numbers = [int(num1), int(num2), int(num3), int(num4), int(num5)]
numbers.sort()
print("The largest number is ", numbers[-1])
