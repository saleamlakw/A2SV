# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph=defaultdict(list)

        def dfs(node):
            if not node:
                return 
            if node.left :
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right :
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        queue=deque([[target.val,0]])
        visited=set([target.val])

        result=[]
        while queue:
            for _ in range(len(queue)):
                node,level=queue.popleft()
                if level==k:
                    result.append(node)
                for nb in graph[node]:
                    if nb not in visited:
                        queue.append([nb,level+1])
                        visited.add(nb)
        return result
         


            