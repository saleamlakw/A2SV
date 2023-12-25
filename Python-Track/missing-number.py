class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        re=set(range(min(nums),max(nums)+1)).difference(set(nums))
        return list(re)[0] if re else  (max(nums)+1 if 0 in nums else 0)