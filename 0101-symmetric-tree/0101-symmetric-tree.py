# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        pairs = [(root.left,root.right)]
        i = 0

        while i < len(pairs):
            a,b = pairs[i]
            i += 1

            # both are empty
            if not a and not b:
                continue
            # one is empty
            if not a or not b:
                return False
            # values are not the same
            if a.val != b.val:
                return False
            
            pairs.append((a.left,b.right))
            pairs.append((a.right,b.left))
            
        return True