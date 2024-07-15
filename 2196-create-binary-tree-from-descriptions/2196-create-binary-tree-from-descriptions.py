# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes=set()
        parents=defaultdict(int)
        all=defaultdict(lambda : [None,None])
        for parent,child,isleft in descriptions:
            parents[child]+=1
            nodes.add(parent)
            nodes.add(child)
            if isleft:
                all[parent][0]=child
            else:
                all[parent][1]=child
                
        root=0
        for ele in nodes:
            if parents[ele]==0:
                root=TreeNode(ele)
       
        
        
        def btree(node):
            
            if all[node.val][0]:
                node.left=btree(TreeNode(all[node.val][0]))
            if all[node.val][1]:
                node.right=btree(TreeNode(all[node.val][1]))
            return node
        return btree(root)
        
        
        