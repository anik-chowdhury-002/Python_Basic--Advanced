n = int(input())

arr = list(map(str,input().strip().lower()))

#arr = []

#for _ in range(n):
	#arr.append(input().strip().lower())

freq = dict()

for colour in arr:
	if colour in freq:
		freq[colour] += 1
	else:
		freq[colour] =1
found = False

for colour in arr:
	if freq[colour] % 2 !=0:
		print(colour)
		found = True
		break
if not found:
	print("All are even")