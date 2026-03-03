result = []
num = int(input("Enter the number : "))
if num<=1:
	print("Not a prime number")
else:
	for i in range(1, num//2 + 1):
		if num % i == 0:
			result.append(i)
	result.append(num)
	print("number of factors",result)

	if result == [1, num]:
    		print("Prime number")
	else:
    		print("Not a prime number")