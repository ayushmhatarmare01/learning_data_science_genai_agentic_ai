#Input annual taxable income.
#For this exercise only, use these simplified slabs: first ₹3,00,000 taxed at 0%;
# next ₹3,00,000 at 5%; next ₹4,00,000 at 10%;
#  income above ₹10,00,000 at 20%. 
#Calculate tax progressively, not by applying one rate to the whole income.
#Reject negative income

annual_income=int(input("Enter your annual income : "))
if annual_income<0:
    print("Invalid Income")
else:
    if annual_income<=300000:
        tax= 0
    elif annual_income<=600000:
        tax=(300000*0/100)+((annual_income-300000)*5/100)
    elif annual_income<=1000000:
        tax=(300000)*5/100+((annual_income -600000)*10/100)
    else:
        tax = (300000 * 5 / 100) + (400000 * 10 / 100) + ((annual_income - 1000000) * 20 / 100)
    print("Tax :",tax)
