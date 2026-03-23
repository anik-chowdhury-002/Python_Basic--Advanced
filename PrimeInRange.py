start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    if num > 1:  # Check if the number is greater than 1
        for i in range(2, int(num**0.5) + 1):  # Check for factors up to the square root of num
            if num % i == 0:  # If num is divisible by any number other than 1 and itself
                break
        else:
            print(num)  # If no factors found, num is prime and we print it