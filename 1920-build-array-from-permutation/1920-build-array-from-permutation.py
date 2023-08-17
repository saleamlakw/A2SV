class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(max(nums)+1):
            ans.append(nums[nums[i]])
        return ans
            