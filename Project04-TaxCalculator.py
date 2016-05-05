"""
Tax Calculator - Asks the user to enter a cost
and either a country or state tax. It then
returns the tax plus the total cost with tax.
"""

cost = float(input("How much was your purchase? >> "))
tax_rate = float(input("What is the tax rate percentage? >> "))

tax_rate = tax_rate/100
total_cost = (cost * tax_rate) + cost
total_tax = total_cost - cost

print("Your total cost is: " + "${0:.2f}".format((total_cost)))
print("Your total tax is: " + "${0:.2f}".format((total_tax)))

