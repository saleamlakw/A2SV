# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        leafs=[]
        graph=defaultdict(list)

        def dfs(node):
            if not node.left and not node.right:
                leafs.append(node.val)
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
      
        def bfs(start,des):
            visited=set([start])
            queue=deque([start])
            distance=0
            while queue:
                for _ in range(len(queue)):
                    node=queue.popleft()
                    if node==des:
                        return distance
                    for  nb in graph[node]:
                        if nb not in visited:
                            queue.append(nb)
                            visited.add(nb)
                distance+=1
       
        
        ans=0
        for i in range(len(leafs)-1):
            if bfs(leafs[i],leafs[i+1])<=distance:
                ans+=1
        return ans
            