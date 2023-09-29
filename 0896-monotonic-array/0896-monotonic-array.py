class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        print(list(reversed(sorted(nums))))
        if nums==sorted(nums) or nums==list(reversed(sorted(nums))):
            return True
        else:
            return False