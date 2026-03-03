n = int(input("Enter the number of elements in the list : "))
nums = []

for i in range(n):
	value = int(input("Enter the Number: "))
	nums.append(value)
print(nums)

lenth = len(nums)

frequency = {}
for i in range(0,lenth + 1):
	if nums[i] in frequency:
		frequency[nums[i]] +=1
	else:
		frequency[nums[i]] = 1
print(frequency)
