# Take monthly income and expenses and print total expenses, remaining balance, and savings status.
mon_inc = float(input("Monthly Income:"))
rent = float(input("Rent:"))
food = float(input("Food:"))
travel = float(input("Travel:"))
tot_exp = rent + food + travel
print("Total Expenses:", tot_exp)
rem_bal = mon_inc - tot_exp
print("Remaining Balance:", rem_bal)
sav_status = rem_bal > 0
print("Savings Status", sav_status)