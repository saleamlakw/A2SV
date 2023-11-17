class Solution:
    def removeDuplicates(self,nums):
        placeHolder=seeker=0
        while seeker<len(nums):
            if nums[placeHolder]!=nums[seeker]:
                nums[placeHolder+1],nums[seeker]=nums[seeker],nums[placeHolder+1]
                placeHolder+=1
            seeker+=1
        print(nums)
        return placeHolder+1
        