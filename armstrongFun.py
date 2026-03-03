def count_digits(num):
	count = 0
	temp = num
	while temp > 0:
		temp = temp // 10
		count = count + 1
	return count


def armstrong(num):
	length = count_digits(num)
	temp = num
	total = 0
	while temp > 0:
		last_digit = temp % 10
		total = (last_digit ** length) + total
		temp = temp // 10
	return total

def main():
	num = int(input("Enter the number: "))
	if num == armstrong(num):
		print("Armstrong Number ")
	else:
		print("Not a Armstrong Number ")

main()


