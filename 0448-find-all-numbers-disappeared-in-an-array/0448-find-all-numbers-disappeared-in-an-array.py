class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]>0:
                 nums[abs(nums[i])-1]=-1*nums[abs(nums[i])-1]

        re=[]
        for k in range(1,len(nums)+1):
            if nums[k-1]>0:
                re.append(k)
        return re