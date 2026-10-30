# Take a three-digit integer as input. Check whether it is actually a three-digit number.
#  If valid, determine whether it is divisible by both 3 and 5, divisible by only one of them, or divisible by neither

number=int(input("Enter a three Digit number: "))
if (number <= 999 and number >= 100) or (number >= -999 and number <= -100):
    print("Number is Three digit number")
    if number % 3 == 0 and number % 5==0:
        print("Divisible by both 3 and 5")
    elif number % 3==0 or number % 5==0:
        print("Divisible by only one of them")
    else:
        print("Not divisible by 3 and 5")

else:
    print("Enter Three digit number")
