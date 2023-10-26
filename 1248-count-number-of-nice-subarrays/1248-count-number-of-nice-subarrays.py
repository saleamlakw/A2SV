class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for j in range(len(nums)):
            if nums[j]%2==1:
                nums[j]=1
            else:
                nums[j]=0
        # print(nums)
        prefix=defaultdict(int)
        prefix[0]=1
        cur=0
        result=0
        for i in nums:
            cur+=i
            result+=prefix[cur-k]
            prefix[cur]+=1
        return result
            