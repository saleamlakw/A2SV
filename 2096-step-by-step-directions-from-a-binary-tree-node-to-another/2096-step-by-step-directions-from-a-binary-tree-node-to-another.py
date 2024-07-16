# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        nodes=defaultdict(lambda : [0,0,0])
        graph=defaultdict(list)
        def dfs(node):
            if node.left:    
                graph[node.val].append(node.left.val)    
                graph[node.left.val].append(node.val)

                nodes[node.left.val][0]=node.val
                nodes[node.val][1]=node.left.val
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                nodes[node.right.val][0]=node.val

                nodes[node.val][2]=node.right.val
                dfs(node.right)
        dfs(root)
        #print(nodes)
        #print(graph)
        
        def bfs():
            parents=defaultdict()
            parents[startValue]=-1
            queue=deque([startValue])
            visited=set([startValue])
            
            while queue:
                for _ in range(len(queue)):
                    node=queue.popleft()
                    if node==destValue:
                        queue=[]
                        break
                    for nb in graph[node]:
                        if nb not in visited:
                            queue.append(nb)
                            visited.add(nb)
                            parents[nb]=node
            result=[]
            re=destValue
            #print(parents)
            while re!=-1:
                result.append(re)
                re=parents[re]
            return result[::-1]
        arr=bfs()
        ans=[]
        for i in range(len(arr)-1):
            if nodes[arr[i]][0]==arr[i+1]:
                ans.append("U")
            elif nodes[arr[i]][1]==arr[i+1]:
                ans.append("L")
            else:
                ans.append("R")
        return "".join(ans)
        
    
            
        
                
        
        
        