# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        direction = [[0,1],[1,0],[0,-1],[-1,0],]
        visited=set()
        mat=[[-1]*n for _ in range(m)]
        def inbound(r,c):
            return 0<=r<m and 0<=c<n
        def check(r,c):
            temp=False
            for rr,cc in direction:
                temp =temp or (inbound(r+rr,c+cc)  and (r+rr,c+cc) not in visited)
            return temp
        def dfs(r,c,node,i):
            
            if not node:
                return 
            # print(check(r,c))
            if not check(r,c):
                return 
            # print(r,c,node.val,i)
            mat[r][c]=node.val
            visited.add((r,c))
            rr,cc=direction[i]
            if inbound(r+rr,c+cc) and (r+rr,c+cc) not in visited:
                dfs(r+rr,c+cc,node.next,i)
            else:
                ind=i+1 if (i+1)<4 else 0
                dfs(r,c,node,ind)
        dfs(0,0,head,0)
        return mat

        
    