# Take the monthly salary as input and calculate: yearly salary, savings (assume 20% savings)
mon_sal = int(input("Enter your monthly salary:"))
yr_sal = mon_sal * 12
yr_sav = (mon_sal*0.20)*12
print("Your annual salary is", yr_sal, "and your annual savings are", yr_sav)