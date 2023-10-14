class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum=[0]
        for num in nums:
            self.prefixsum.append(self.prefixsum[-1]+num)
    def sumRange(self, left: int, right: int) -> int:
        return (self.prefixsum[right+1]-self.prefixsum[left])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)