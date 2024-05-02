class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor=0
        for ele in nums:
            xor^=ele
        return (xor^k).bit_count()