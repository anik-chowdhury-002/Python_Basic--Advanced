import math

num = int(input("Enter the number: "))

num = abs(num)   # handle negative numbers

if num == 0:
    digits = 1
else:
    digits = int(math.log10(num)) + 1   # take integer part

print("Number of digits:", digits)
