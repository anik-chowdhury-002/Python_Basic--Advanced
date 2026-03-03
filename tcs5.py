start_day = input().strip().lower()

n = int(input())

days = ["mon","tue","wed","thu","fri","sat","sun"]

start_index = days.index(start_day)

count = 0

for i in range(n):
	if(start_index + i) % 7 == 6:
		count = count + 1
print(count)
