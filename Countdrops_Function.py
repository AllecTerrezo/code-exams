import math 

def count_drops(limit_floor: int, eggs: int) -> int:

    if limit_floor>100:
        return "Limit above the allowed, please pass a number equal or bellow 100."
    
    else:

        # Number of covered floors (Arithmetic Progression Sum of floors per egg used): k + (k-1) + (k-2) + ... + 1 = k*(k+1)/2 

        # Covered floors <= limit_floor 

        # k*(k+1)/2 <= limit_floor 

        # k^2 + k - 2*limit_floor <= 0 

        # Using Bhaskara formula to discover positive k. ((-b + sqrt(b^2 -4ac))/2): k = (-1 + sqrt(1 + 8*floors)) / 2 

            number_drops = (math.sqrt(1 + 8*limit_floor) -1) // 2

        # Number of floors covered by drops
            
            covered_floors = number_drops * (number_drops + 1) // 2

        #Using the lost egg we can understand how many floors are left and verifying if there are eggs and floors we can sum the Number of drops in the current attempt with the result of calling the count_drops function recursively

            left_floors = limit_floor - covered_floors
            eggs_quantity = eggs - 1
            if eggs_quantity > 0 and left_floors > 0:
                return int(number_drops + count_drops(left_floors, eggs_quantity))

        # If eggs_quantity or left_floors equals 0 return the value of Number of drops

            return int(number_drops)

#Example
print(count_drops(63, 2))