class Solution(object):
    def pivotIndex(self, nums):
            prefixSum=[]
            accumulator=0
            for r in nums:
                accumulator+=r
                prefixSum.append(accumulator)
            
            
            postfixSum=deque()
            accumulator=0
            for l in nums[::-1]:
                accumulator+=l
                postfixSum.appendleft(accumulator)
            
            for i in range(len(prefixSum)):
                if prefixSum[i]==postfixSum[i]:
                    return i
            return -1