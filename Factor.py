from math import sqrt
result = []
num = int(input("Enter the numbe...to which you want to calculate the factor : "))

for i in range (1,int(sqrt(num))+1):
	if num % i == 0:
		result.append(i)
		if num // i != i:
			result.append(num//i)
result.sort()
print(result)