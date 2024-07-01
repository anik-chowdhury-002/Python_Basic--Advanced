def factorial(a):
    if a==0:
        return 1
    else:
        #using recursion
        return((a)*factorial(a-1))
    
num = int(input("Enter the number which you want to calculate factorial : "))
result = factorial(num)
print("The factorial of the given number is " , result)

