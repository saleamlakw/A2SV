class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset,cursubset=[],[]
        self.helper(0,nums,subset,cursubset)
        return subset
    def helper(self,i,nums,subset,cursubset):
        if i>=len(nums):
            subset.append(cursubset.copy())
            return 
        cursubset.append(nums[i])
        self.helper(i+1,nums,subset,cursubset)
        cursubset.pop()
        self.helper(i+1,nums,subset,cursubset)
