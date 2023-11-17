class Solution(object):
    def minDeletion(self, nums):
        stack=[]
        result=0
        l=r=0
        while r < len(nums):
            # print(l-1)
            if stack and (l-1)%2==0:
                
                while r<len(nums) and stack and (l-1)%2==0 and stack[-1]==nums[r]:
                    r+=1
                    result+=1
                if r<len(nums):
                    stack.append(nums[r])
                    l+=1
                # print(stack)
            else:
                stack.append(nums[r])
                l+=1
                # print(stack)
            r+=1
        if len(stack)%2!=0:
                result+=1
        return result
            
        