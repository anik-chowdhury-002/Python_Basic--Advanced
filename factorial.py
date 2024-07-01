num = int(input("Enter the number which you want to calculate factorial : "))
factorial = 1
if num<0:
    print("Factorial calculation is not possible : ")
if num==0:
    print("Factorial of 0 is 1")
else:
    #using for loop
    for i in range (1,num+1):
        factorial = factorial*i
print("factorial of the given number is : ",factorial)