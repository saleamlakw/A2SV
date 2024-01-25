class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cc=Counter()
        result=0

        ps=list(accumulate(nums))
        for ele in ps:
            if ele==k:
                result+=1
            if ele-k in cc:
                result+=1*cc[ele-k]
            cc[ele]+=1
        return result