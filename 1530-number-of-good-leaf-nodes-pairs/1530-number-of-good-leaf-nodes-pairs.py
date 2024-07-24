# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leafs=set()
        graph=defaultdict(list)

        def dfs(node):
            if not node.left and not node.right:
                leafs.add(node)
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs(node.right)
        dfs(root)

        
        ans=0
        def bfs(start):
            nonlocal ans
            visited=set([start])
            queue=deque([start])
            dist=0
            while queue:
                for _ in range(len(queue)):
                    if dist>distance:
                        return 
                    node=queue.popleft()
                    if node !=start and node in leafs and dist<=distance:
                            ans+=1
                    for  nb in graph[node]:
                        if nb not in visited:
                            queue.append(nb)
                            visited.add(nb)
                dist+=1
       
        
     
        for ele in leafs:
            bfs(ele)       
        return ans//2
            