num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
num3 = int(input("Enter the 3rd number : "))

if(num1>num2) and (num1>num3):
    print("Number 1 is the largest number")
elif(num2>num1) and (num2>num3):
    print("Number 2 is the largest number")
else:
    print("Number 3 is the largest number")
