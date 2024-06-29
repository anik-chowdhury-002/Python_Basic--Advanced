#check the given number is prime or not
#prime number is a number who is divisible only by one and that number itself 

num = int(input("Enter the number:"))
if num == 1:
    print("This is not an prime number : ")
if num > 1:
    for i in range (2,num):
        if(num%i == 0):
            print("This is not an prime number")
            break;
        else:
            print("This a prime number : ")
            break;