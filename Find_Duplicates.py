def find_duplicates(nums: list) -> list:
    values = [] # List Created to Store Duplicates

    nums_size = len(nums) # Number of items in the list

# Iterate through the list poping elements and verifying if these elements has other values in the nums list and in the values list
    for item in range(0,nums_size):
        number = nums.pop(0) #Pop the first element of the list
        if number in nums: # If there are equal values to the number poped in nums list
            if number in values: # If there are equal values to the number poped in values list
                pass # Pass as the value already exist in the values list
            else:
                values.append(number) #Append the value poped to the values list as it exists in nums and doesn't exist in values list 

    return values

# Example:
numbers = [1, 1, 1, 2, 3, 4, 1, 5, 2, 7, 8, 5, 10, 10,10, 2,10,10]
print(find_duplicates(numbers)) # Result: [1, 2, 5, 10]
