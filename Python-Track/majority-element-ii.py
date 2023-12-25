class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        hashmap=Counter(nums)
        for r in hashmap:
            if hashmap[r]>len(nums)/3:
                result.append(r)
        return result

        