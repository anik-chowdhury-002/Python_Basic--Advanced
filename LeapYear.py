year = int(input("Enter  the year : "))

if(year%400==0) and (year%100==0):
    print("This is a leap year : ")
elif(year%4==0) and (year%100 != 0):
    print("This is also a leap lear : ")
else:
    print("This is not an leap year : ")