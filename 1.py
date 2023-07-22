# Geek has a Remote Controlled Car that can only jump forward or backward by a fixed distance 'k' with each button press. The car cannot turn right or left.

# Given a string 'moves' representing the sequence of moves ('F' for forward and 'B' for backward) for each second, help Geek find the count of unique positions that his car will jump to.

# Example 1:

# Input:
# k = 2
# moves = "FBFB"


# Output: 2
class Solution:
    def uniquePositions(self, moves: str, k: int) -> int:
        # code here
        position = 0
        positions = set([position])
        for move in moves:
            if move == "F":
                position += k
            elif move == "B":
                position -= k
        positions.add(position)
        return len(positions)
