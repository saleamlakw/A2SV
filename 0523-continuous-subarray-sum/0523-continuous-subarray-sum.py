class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap=Counter()
        hashmap[0]+=1

        tot=0
        result=0
        result2=0
        for num in nums:
            if num%k==0:
                result2+=1
            tot+=num
            result+=hashmap[tot%k]
            hashmap[tot%k]+=1
        
        return (result-result2)>0
