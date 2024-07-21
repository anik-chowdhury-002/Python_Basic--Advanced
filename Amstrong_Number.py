
num = int(input("Enter the number you want to check : that that is amstrong or not "))
order = len(str(num))
sum = 0
temp = num
while temp>0:
    digit  = temp % 10 #obtain the last digit of the number 
    power = digit**order
    sum = sum + power
    temp //= 10 #remove the last digit 
if(sum==num):
    print('It is an amstrong number  ')
else:
    print('It is not an amstrong number ')

