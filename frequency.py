nums = list(map(int, input("Enter Numbers: ").split()))
print(nums)
lenth = len(nums)

frequency = dict()
for i in range(0,lenth):
	if nums[i] in frequency:
		frequency[nums[i]] +=1
	else:
		frequency[nums[i]] = 1
print(frequency)





