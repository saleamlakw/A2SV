class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        dp=[[float("inf")]*(1<<n) for _ in range(n)]
        
        for i in range(n-1,-1,-1):
            for mask in range((1<<n)-1,-1,-1):
                temp=float("inf")
                for j in range(n):
                    if  mask&(1<<j):
                        continue
                    res=dp[i+1][mask|(1<<j)] if (i+1)<n else 0
                    temp=min(temp,(nums1[i]^nums2[j])+res) 
                dp[i][mask]=temp
                # print(dp)
        return dp[0][0]
       