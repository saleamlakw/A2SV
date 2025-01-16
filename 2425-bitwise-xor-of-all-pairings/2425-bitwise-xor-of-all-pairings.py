class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        xor_1 = 0
        for num in nums1:
            xor_1 ^= num
        
        xor_2 = 0
        for num in nums2:
            xor_2 ^= num
        
        return ((m % 2)*xor_1) ^ ((n % 2)*xor_2)


