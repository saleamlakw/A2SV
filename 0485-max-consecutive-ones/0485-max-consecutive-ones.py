class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        re=0
        window=Counter()
        l=0
        for r in range(len(nums)):
            window[nums[r]]+=1
            while window[0]>0:
                if nums[l]==0:
                    window[0]-=1
                    if window[0]==0:
                        window.pop(0)
                l+=1
            re=max(re,r-l+1)
        return re
            
            