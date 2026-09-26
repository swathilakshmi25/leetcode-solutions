from itertools import pairwise

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Bottom-up DP: Initialize with the absolute base case row
        res = [[1]]
        
        # Loop exactly numRows - 1 times to build the rest of the triangle
        for _ in range(numRows - 1):
            # Every row in Pascal's Triangle begins with a 1
            new_row = [1]
            
            # pairwise() iterates over overlapping adjacent pairs from the previous row (res[-1]).
            # e.g., if res[-1] is [1, 2, 1], pairwise yields (1, 2) and (2, 1).
            for a, b in pairwise(res[-1]):
                new_row.append(a + b)
                
            # Every row in Pascal's Triangle ends with a 1
            new_row.append(1)
            
            # Store the computed row into our DP tabulation table
            res.append(new_row)
            
        return res