n = int(input())

arr = []
for _ in range(n):
    arr.append(input().strip())

prefix = arr[0]

for word in arr[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            break

print(prefix)