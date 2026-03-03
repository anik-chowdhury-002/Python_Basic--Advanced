num = int(input("Enter the number : "))

count = 0
num = abs(num)

if num == 0:
    count = 1
else:
    while num > 0:
        count = count + 1
        num = num //10
print("Number of Digit is ", count)


