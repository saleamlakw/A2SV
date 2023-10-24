from itertools import accumulate
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr1=list(accumulate(nums))
        arr2=list(accumulate(nums[::-1]))[::-1]
        for i in range(len(arr1)):
            if arr1[i]==arr2[i]:
                return i
        return -1
        