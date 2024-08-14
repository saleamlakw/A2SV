class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def check(d):
            # print(d)
            count=0
            l=0
            for r in range(len(nums)):
                while nums[r]-nums[l]>d:
                    l+=1
                if nums[r]-nums[l]<=d:
                    count+=(r-l)
            # print("c",count)
            return count>=k

        l,r=0,max(nums)*2
        ans=float("inf")
        while r>=l:
            m=(l+r)//2
            if check(m):
                ans=min(ans,m)
                r=m-1
            else:
                l=m+1
        return ans




