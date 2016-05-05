"""
Find Cost of Tile to Cover W x H Floor -
Calculate the total cost of tile it would
take to cover a floor plan of width and
height, using a cost entered by the user.
"""

cost = int(input("How much does the tile cost per square foot? >> "))
length = int(input("What is the length of the area? >> "))
width = int(input("What is the width of the area? >> "))

sq_ft = width * length
total_cost = sq_ft * cost
print('Your tile will cost $' + str(total_cost))