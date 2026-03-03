n = int(input())

#arr = list(map(int,input().split()))[:n]

arr=[]

for _ in range(n):
	arr.append(int(input()))

count = 1
max_upto = arr[0]

for i in range(1,n):
	if arr[i]>max_upto:
		count += 1
		max_upto = arr[i]
print(count)
