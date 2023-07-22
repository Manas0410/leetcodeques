# In Geekland, there are 'n' cities connected by 'n - 1' bidirectional roads, forming a connected and weighted undirected tree. Geek wants to go on a long drive with Geekina, ensuring he visits each city at most once during the trip to avoid making Geekina angry.


# Geek has 'q' possible options to start his trip, given in an array query[ ]. The task is to help Geek find the longest distance he can travel starting from each city given in the 'query' array.
# Input:
# n = 5


# edges[][] = [[1, 5, 3],
#              [2, 5, 3],
#              [1, 4, 2],
#              [5, 3, 2]]
# q = 4
# query[] = [1, 3, 4, 5]
# Output:
# 6 7 8 5
# Explanation:
# From city 1, longest distance is 1 -> 5 -> 2 = 6.
# From city 3, longest distance is 3 -> 5 -> 1 -> 4 = 7.
# From city 4, longest distance is 4 -> 1 -> 5 -> 2 = 8.
# From city 5, longest distance is 5 -> 1 -> 4 = 5.
