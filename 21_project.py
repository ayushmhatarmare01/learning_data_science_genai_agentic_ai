#Input account balance and withdrawal amount. 
# Reject negative values, reject withdrawals greater than the balance
#  allow withdrawals only in multiples of ₹100. 
# If valid, show the remaining balance.

account_balance=int(input("Enter the account balance: "))
if account_balance<0 :
    print("Invalid Account balance")
else:  
    withdrawal_amount=int(input("Enter the withdrawal amount: "))
    if withdrawal_amount<=0 or withdrawal_amount>account_balance:
        print("insufficent balance")
    elif withdrawal_amount%100!=0:
        print("Please Enter the amount in multiple of 100")
    else:
        print("Withdrawal Successfully @@@@@")
        Remining_balance=account_balance - withdrawal_amount
        print("Remining balance : ",Remining_balance)
