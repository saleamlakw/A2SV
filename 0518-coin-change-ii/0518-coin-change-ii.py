class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        def dp(pre,target):
            if target==0:
                return 1
            if target<0:
                return 0
            if (pre,target) not in memo:
                re=0
                for i in range(len(coins)):
                    if coins[i]>=pre:
                        re+=dp(coins[i],target-coins[i])
                memo[(pre,target)]=re
            return memo[(pre,target)]
        return dp(float("-inf"),amount)
