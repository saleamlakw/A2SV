class NumArray:
    from itertools import accumulate
    def __init__(self, nums: List[int]):
        self.nums=nums
        self.Psum=list(accumulate(self.nums))
    def sumRange(self, left: int, right: int) -> int:
        return (self.Psum[right]-self.Psum[left-1]) if left!=0 else self.Psum[right]
