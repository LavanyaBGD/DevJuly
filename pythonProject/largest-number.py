num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
num3=int(input("Enter a third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest of the three numbers is {largest}")
