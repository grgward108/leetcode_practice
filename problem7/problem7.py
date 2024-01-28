# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def count_helper(root, max_val):
            if root is None:
                return 0
            
            res = 1 if root.val >= max_val else 0                
            max_val = max(root.val, max_val)

            res += count_helper(root.left, max_val)
            res += count_helper(root.right, max_val)
        
            return res
        
        return count_helper(root, float('-inf'))