num = int(input("Enter the number:"))
	
storted_number = num
result = 0

while num > 0:
	last_digit = num % 10
	result = (result * 10) + last_digit
	num = num // 10
print("The reverse of the number is:", result)

if storted_number == result:
	print("This is a palindrome number :" )
else:
	print("This number is not a palindrome number :" )