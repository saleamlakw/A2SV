class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        accumulator=0
        hashmap=Counter()
        hashmap[0]+=1
        result=0
        for num in nums:
            
            accumulator+=num
            result+=hashmap[accumulator%k]
            hashmap[accumulator%k]+=1

        return result
