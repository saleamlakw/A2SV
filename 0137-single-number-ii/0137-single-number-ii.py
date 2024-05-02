class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones=0
        twos=0
        for ele in nums:
            ones=(ones^ele)& ~twos
            twos=(twos^ele)& ~ones
        return ones
