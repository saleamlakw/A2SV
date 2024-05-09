class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        def bitOn(n,k):
            return n&(1<<k)!=0

        xor=0
        for ele in nums:
            xor^=ele
        # print(xor)
        result=[]
        for i in range(len(nums)-1,-1,-1):
            x=0
            for j in range(maximumBit):
                if bitOn(xor,j):
                    x=x&(~(1<<j))
                else:
                    x=x|1<<j           
            result.append(x)
            xor^=nums[i]
        return result