class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        def bitOn(n,k):
            return n&(1<<k)!=0

        xor=0
        for ele in nums:
            xor^=ele
        result=[]
        for i in range(len(nums)-1,-1,-1):
            x=(xor&((1<<(maximumBit))-1))
            x^=(1<<(maximumBit))-1         
            result.append(x)
            xor^=nums[i]
        return result