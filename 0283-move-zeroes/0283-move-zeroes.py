class Solution(object):
    def moveZeroes(self, nums):
        placeholder=0
        for seeker in range(len(nums)):
            while placeholder <len(nums) and nums[placeholder]!=0:
                placeholder+=1
            if placeholder <len(nums) and nums[placeholder] ==0 and nums[seeker]!=0 and seeker>placeholder:
                nums[placeholder],nums[seeker]=nums[seeker],nums[placeholder]
        # return nums
"""
1) approch use seeker and placeholder technique which is the varation of two pointer 
2)plce holder to hold zeros 
3)seeker to seek non zero number 
4)once we get zero in place holder and non zero number in the seeker pointer swap the place holder and seeker 
5)continue this step this until all zero move to the end of the array 
"""
    
        