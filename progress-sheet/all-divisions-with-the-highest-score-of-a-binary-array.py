class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        one=nums.count(1)
        zero=0
        hashmap=defaultdict(list)
        hashmap[one+zero].append(0)
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one-=1
            hashmap[one+zero].append(i+1)
        k=max(hashmap.keys())
        return hashmap[k]
