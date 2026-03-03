s = input().strip()

star_count = 0
hash_count = 0

for ch in s:
	if ch == "*":
		star_count = star_count + 1
	elif ch == "#":
		hash_count = hash_count + 1
result = star_count - hash_count
print(result)