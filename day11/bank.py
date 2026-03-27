withdrawal_amt = int(input("Enter the withdrawal amount (multiple of 100) : "))

balance = int(input("Enter the balance amount : "))

# if withdrawal_amt < balance and balance - withdrawal_amt >= 500 :

#     balance -= withdrawal_amt
#     print(f"Transaction Successful...Remaining balance is {balance}..")

# else :

#     print("Transaction Failed ")

print("Transaction Success" if withdrawal_amt < balance and balance - withdrawal_amt >= 500 else "Transaction Failed")