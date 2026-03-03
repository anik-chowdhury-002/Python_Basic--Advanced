num = int(input("Enter the number: "))

s_num = str(num)

rev = ''.join(reversed(s_num))

if s_num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
