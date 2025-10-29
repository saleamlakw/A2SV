# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        node = root
        prev = -inf
        stack = [node]

        while stack:
            while node and node.left:
                stack.append(node.left)
                node = node.left
            
            node = stack.pop()
            if node.val <= prev:
                return False
            
            prev = node.val

            if node.right:
                node = node.right
                stack.append(node)
            
            else:
                node = None
        
        return True
        

      
    
