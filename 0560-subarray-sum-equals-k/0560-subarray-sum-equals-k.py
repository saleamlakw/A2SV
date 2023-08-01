class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        cur=0
        res=0
        for i in nums:
            cur+=i
            res+=dic.get(cur-k,0)
            dic[cur]=1+dic.get(cur,0)
        return res
                
        