# Geek is travelling from Geek Land to Destination Land. He has access to n magical spells that can boost his car's speed. Each spell, when cast at the exact time spells[i], instantly increases the car's speed to k meters per second and then decreases by 1 meter per second until it reaches 0.

# Geek needs to cover at least trackLength distance to reach Destination Land. Help him find the minimum value of k required to complete the journey.

# Example 1:

# Input:
# trackLength = 20
# n = 3
# spells = [1, 5, 9]

# Output: 4

# Explanation:
# Geek casts a spell at time = 1, his car's speed reaches k = 4 m/s.
# During the 1st second, the car moves 4 meters, 3 meters in the 2nd second, 2 meters in the 3rd second, and 1 meter in the 4th second.
# By then, his car has moved a total of 10 meters.
# If he casts the spell again in the 5th second, the car will move another 10 meters, completing the trackLength.
