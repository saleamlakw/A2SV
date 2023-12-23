class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        p1,p2=0,n
        while p1 <n and p2<len(nums):
            result.append(nums[p1])
            result.append(nums[p2])
            p1+=1
            p2+=1
        return result