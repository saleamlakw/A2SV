class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        tot=0
        res=0
    
        for num in nums:
            if tot>=n:
                return res
            # print(tot,num)
            num=min(n+1,num)
            while num>(tot+1):
                tot+=(tot+1)
                res+=1
            else:
                tot+=num
            # print(res)
        while tot<n:
            tot+=(tot+1)
            res+=1
        return res
          

                       