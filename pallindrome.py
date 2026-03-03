num = int(input("Enter the number: "))

s_num = str(num)
rev = s_num[::-1]
if s_num == rev:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")
