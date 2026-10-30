#Input a year and determine whether it is a leap year.
# A year is a leap year if divisible by 400, or divisible by 4 but not by 100.
#  Reject years less than or equal to zero
 
year=int(input("Enter the year : "))
if year<=0:
    print("Year is not in negative/zero")
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Year is leap year")
    else:
        print("Not a leap year")
