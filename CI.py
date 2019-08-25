#finding out how much money is in the account 
money_in_acc = int(input("How much money is in the account?:"))

#finding out is the compound daily, quarterly, or yearly
dqy = int(input("Is the Compounding interest daily, qaurterly, or yearly? for daily type: 1, for quarterly type: 2, for yearly type: 3:" ))

#finding out what the interest rate is in decimal
interest_rate = float(input("What is the interest rate in decimal? for example 10% = 0.1:"))

#finding out how far out they'd like to calculate
years_out = input("How many years out would you like to calculate?:")

if dqy == 1: 
    for x in years_out * 365: 
        money_in_acc = money_in_acc * (1 + interest_rate)
    print(money_in_acc)
elif dqy == 2: 
    for x in years_out * 4: 
        money_in_acc = money_in_acc * (1 + interest_rate)
    print(interest_rate)
elif dqy == 3: 
    for x in years_out: 
        money_in_acc = money_in_acc * (1 + interest_rate)
    print(money_in_acc)
else: 
    print("error")
