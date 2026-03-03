num = int(input("Enter the number : "))
stored_num = num
result = 0

while num > 0:
    Last_igit = num % 10
    result = (result * 10) + Last_igit
    num = num // 10
print(result)
if stored_num == result:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")