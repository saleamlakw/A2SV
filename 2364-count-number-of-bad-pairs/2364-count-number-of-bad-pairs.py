class Solution(object):
    def countBadPairs(self, nums):
        hashmap = Counter()
        goodPairs = 0
        for i in range(len(nums)):
            goodPairs += (hashmap[i-nums[i]])
            hashmap[i-nums[i]]+=1
        n = len(nums)
        allPairs = (n*(n-1))//2
        return allPairs - goodPairs

            
        