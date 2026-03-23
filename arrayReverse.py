arr = list(map(int, input("Enter the elements of the array : ").split()))

left = 0
right = len(arr) - 1

def arrReverse(arr,left,right):
	if left>=right:
		return
	arr[left],arr[right] = arr[right],arr[left]
	arrReverse(arr,left+1,right-1)

arrReverse(arr,left,right)
print(*arr)



