class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        al=[]
        for i in set(nums):
            al.append([i,nums.count(i)])
        al.sort(reverse=True,key=lambda x:x[1])
        return [al[j][0] for j in range(k) ]
