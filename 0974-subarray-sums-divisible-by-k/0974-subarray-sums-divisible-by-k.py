class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap=Counter()
        hashmap[0]+=1
        result=0
        tot=0
        for num in nums:
            tot+=num
            result+=hashmap[tot%k]
            hashmap[tot%k]+=1
        return result
