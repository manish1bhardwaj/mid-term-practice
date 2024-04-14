import math

def min_steps_to_girlfriends_house(x):
    # Calculate the minimum number of steps required
    # Each step can be of length 5, so divide x by 5 and round up
    steps = math.ceil(x / 5)
    
    return steps

# Read input
x = int(input())

# Calculate and print the result
result = min_steps_to_girlfriends_house(x)
print(result)
