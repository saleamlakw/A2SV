class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        placeholder=0
        seeker=0
        while seeker<len(nums):
            while placeholder<len(nums) and nums[placeholder]!=0:
                placeholder+=1

            if placeholder<len(nums) and seeker<len(nums) and nums[placeholder]==0 and nums[seeker]!=0 and seeker>placeholder :
                nums[placeholder],nums[seeker]=nums[seeker],nums[placeholder]
            seeker+=1
        return nums