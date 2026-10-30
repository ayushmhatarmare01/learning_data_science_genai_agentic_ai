#Input electricity units. 
# The rates are: first 100 units at ₹2/unit, next 100 at ₹5/unit, and units above 200 at ₹8/unit.
# Add a 10% surcharge if the bill exceeds ₹1,000. Reject negative units


electricity_units = int(input("Enter electricity units: "))
if electricity_units < 0:
    print("Invalid units")
else:
    if electricity_units <= 100:
        bill = electricity_units * 2
    elif electricity_units <= 200:
        bill = (100 * 2) + ((electricity_units - 100) * 5)
    else:
        bill = (100 * 2) + (100 * 5) + ((electricity_units - 200) * 8)
    print("Bill before surcharge: ₹", bill)
    if bill > 1000:
        extracharge = bill * 0.10
    else:
        extracharge = 0
    final_bill = bill + extracharge
    print("Surcharge: ₹", extracharge)
    print("Final electricity bill: ₹", final_bill)
            


