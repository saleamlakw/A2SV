class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        curMin=nums[0]
        for i in nums[1:]:
            while stack and i>=stack[-1][0]:
                stack.pop()
            if stack and i>stack[-1][1]:
                return True
            curMin=min(curMin,i)
            stack.append([i,curMin])
        return False
        
        
                
            
                
        