#Write the python code to check the number is Armstrong or not


num = int(input("Enter the number :" ))
original_num = num
total = 0
num_of_dig = len(str(num))

print("The length of the given number is : ", num_of_dig)

while num > 0:
	last_digit = num % 10
	total = total + (last_digit**num_of_dig)
	num = num//10
#print("After all the operation the total number is : ", total)

if original_num == total:
	print("The Given Number is a Armstrong number")
else:
	print("The Given number is not a Armstrong number")




