import math 

def count_drops(floors: int, eggs: int) -> int:

# Number of covered floors: x + (x-1) + (x-2) + ... + 1 = x*(x+1)/2 

# Covered floors <= floors 

# x*(x+1)/2 <= floors 

# x^2 + x - 2*floors <= 0 

# With quadratic formula ((-b + sqrt(b^2 -4ac))/2): x = (-1 + sqrt(1 + 8*floors)) / 2 

    number_drops = (math.sqrt(1 + 8*floors) -1) // 2

# Number of floors covered by drops
    
    covered_floors = number_drops * (number_drops + 1) // 2

#Using the first egg to understand how many floors are left and verifying if there are eggs and floors we can sum the Number of drops in the current attempt with the result of calling the count_drops function recursively

    left_floors = floors - covered_floors
    eggs_quantity = eggs - 1
    if eggs_quantity > 0 and left_floors > 0:
        return int(number_drops + count_drops(left_floors, eggs_quantity))

# If eggs_quantity or left_floors equals 0 return the value of Number of drops

    return int(number_drops)

#Based on the question where we have the limit floor and 2 eggs.

print(count_drops(83, 2))