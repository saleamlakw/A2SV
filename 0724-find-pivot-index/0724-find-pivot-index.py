class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[]
        accumulator=0
        for num in nums:
            accumulator+=num
            prefix.append(accumulator)
        # print(prefix)
        postfix=deque()
        accumulator=0
        for num in nums[::-1]:
            accumulator+=num
            postfix.appendleft(accumulator)
        # print(postfix)  
        for n in range(len(prefix)):
            if prefix[n]==postfix[n]:
                return n
        return -1
        
"""
i will calculate postfix sum of the array and prefix sum the array
i will itertate through both array and find the index in which value in both array is equal
i will use the index to find the the pivot element 
"""