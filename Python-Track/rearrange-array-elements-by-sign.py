class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        for r in nums:
            if r>0:
                positive.append(r)
            else:
                negative.append(r)
        result=[]
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result