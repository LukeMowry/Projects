"""
Mortgage Calculator - Calculate
the monthly payments of a fixed
term mortgage over given Nth terms
at a given interest rate. Also figure
out how long it will take the user to
pay back the loan. For added complexity,
add an option for users to select the
compounding interval (Monthly, Weekly, Daily, Continually).
"""

mortgage = float(input("What is your mortgage amount? >> "))
interest_rate = float(input("What is your yearly interest rate percentage? >> "))
term = float(input("How many years do you plan on holding this mortgage for? >> "))

interest_rate = interest_rate / 100

total_cost = mortgage *  (1 + interest_rate)

monthly_cost = round(total_cost / (term*12), 2)

print("Your monthly cost is $" + str(monthly_cost))
