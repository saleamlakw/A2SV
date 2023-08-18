class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=Counter(nums)
        for i in c:
                while c[i]>2:
                    nums.remove(i)
                    c[i]-=1
        return len(nums)
                
        
        
                
        
        