arr = list(map(int, input("Enter the array elements separated by space: ").split()))

def is_sorted(arr):
    """Check if the array is sorted in non-decreasing order."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print("The array is sorted in non-decreasing order." if is_sorted(arr) else "The array is not sorted in non-decreasing order.")
        
        
