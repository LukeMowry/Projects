"""
Change Return Program - The user
enters a cost and then the amount
of money given. The program will
figure out the change and the number
of quarters, dimes, nickels, pennies needed for the change.
"""

cost = float(input("How much did your purchase cost? >> "))
paid = float(input("How much did you pay? >> "))

dollars = int(paid - cost)
change =  round(paid - dollars - cost, 2)

fifty = 0
twenty = 0
ten = 0
five = 0
one = 0
quarter = 0
dime = 0
nickel = 0
penny = 0

while dollars >= 50:
    dollars -= 50
    fifty += 1
while dollars >= 20:
    dollars -= 20
    twenty += 1
while dollars >= 10:
    dollars -= 10
    ten += 1
while dollars >= 5:
    dollars -= 5
    five += 1
while dollars >= 1:
    dollars -= 1
    one += 1

while change >= .25:
    change -= .25
    quarter += 1
while change >= .10:
    change -= .10
    dime += 1
while change >= .05:
    change -= .05
    nickel += 1
while change >= .01:
    change -= .01
    penny += 1

print("Your change is " + str(fifty) + " fifty dollar bill(s), " + str(twenty) + " twenty dollar bill(s), " +
      str(ten) + " ten dollar bill(s), " + str(five) + " five dollar bill(s), " + str(one) +
      " one dollar bill(s), " + "\n" + str(quarter) + " quarter(s), " + str(dime) + " dime(s), " +
      str(nickel) + " nickel(s), and " + str(penny) + " penny(s).")
print(dollars)

