class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        tot=0
        res=0
        coins.sort()
        for num in coins:
            if tot>=target:
                return res
            tar=min(num,target)
            # print(tot,tar)
           
            while tar>(tot+1):
                res+=1
                tot+=(tot+1)
            if target<num:
                res+=1
                tot+=target
            else:
                tot+=num
           
            # print(res)
        while tot<target:
            tot+=(tot+1)
            res+=1
        
        return res


