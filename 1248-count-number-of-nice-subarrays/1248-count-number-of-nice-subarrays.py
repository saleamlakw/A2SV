class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCount=0
        hashmap=Counter()
        hashmap[0]+=1
        ans=0
        for num in nums:
            if num%2!=0:
                oddCount+=1
            ans+=hashmap[oddCount-k]
            hashmap[oddCount]+=1
        return ans
            