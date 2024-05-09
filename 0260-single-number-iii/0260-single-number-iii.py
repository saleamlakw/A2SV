class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0

        for ele in nums:
            xor^=ele

        first_bit=(xor&(xor-1)^xor)
        n1=0
        for ele in nums:
            if ele&first_bit:
                n1^=ele
        return [n1,xor^n1]