"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue=deque([root])
        
        level=0
        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()

                for nb in node.children:
                    queue.append(nb)
            level+=1
        return level