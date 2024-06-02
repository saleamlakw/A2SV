class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hashmap=Counter()
        hashmap[0]+=1

        accumulator=0
        result=0
        for num in nums:
            accumulator+=num
            result+=hashmap[accumulator-k]
            hashmap[accumulator]+=1
            
        return result

