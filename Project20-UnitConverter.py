"""
Unit Converter (temp, currency, volume, mass and more) -
Converts various units between one another. The user enters
the type of unit being entered, the type of unit they want
to convert to and then the value. The program will then make the conversion.
"""

init_unit = input("Please enter your current unit of temperature. >> ")
fin_unit = input("Now enter the unit you want to convert to. >> ")
amount = int(input("Finally, enter the amount that you are looking to convert. >> "))

def f_to_c(amount):
    print(round((amount - 32) * (5/9), 2))

def c_to_f(amount):
    print(round(amount * (9/5) + 32, 2))

def f_to_k(amount):
    print(round((amount + 459.67) * (5/9), 2))

def k_to_f(amount):
    print(round((amount * (9/5) - 459.67), 2))

def c_to_k(amount):
    print(round(amount + 273.15, 2))

def k_to_c(amount):
    print(round(amount - 273.15, 2))

if (init_unit.lower() == "f" or init_unit.lower() == "fahrenheit") and (fin_unit.lower() == "c" or fin_unit.lower() == "celsius"):
    f_to_c(amount)
elif (init_unit.lower() == "c" or init_unit.lower() == "celsius") and (fin_unit.lower() == "f" or fin_unit.lower() == "fahrenheit"):
    c_to_f(amount)
elif (init_unit.lower() == "f" or init_unit.lower() == "fahrenheit") and (fin_unit.lower() == "k" or fin_unit.lower() == "kelvin"):
    f_to_k(amount)
elif (init_unit.lower() == "k" or init_unit.lower() == "kelvin") and (fin_unit.lower() == "f" or fin_unit.lower() == "fahrenheit"):
    k_to_f(amount)
elif (init_unit.lower() == "c" or init_unit.lower() == "celsius") and (fin_unit.lower() == "k" or fin_unit.lower() == "kelvin"):
    c_to_k(amount)
elif (init_unit.lower() == "k" or init_unit.lower() == "kelvin") and (fin_unit.lower() == "c" or fin_unit.lower() == "celsius"):
    k_to_c(amount)
else:
    print("Those units are invalid.")
