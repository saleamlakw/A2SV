class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        memo={}
        def backtrack(i,mask):
            # print(i,bin(mask)[2:])
            if i>=n:
                return 0
            if (i,mask) not in memo:
                temp=float("inf")
                for j in range(n):
                    if  mask&(1<<j):
                        continue
                    temp=min(temp,nums1[i]^nums2[j]+backtrack(i+1,mask|(1<<j)))
                memo[(i,mask)]=temp
            return memo[(i,mask)]
        return backtrack(0,0)
