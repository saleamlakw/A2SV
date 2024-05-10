class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo=Counter()
        coins.sort(reverse=True)
        def fn(i,target):
            if target in memo:
                return memo[target]
            if target<0:
                return float("inf")
            if target==0:
                return 0
            temp=float("inf")
            if target not in memo:
                for j in range(len(coins)):
                    temp=min(temp,1+fn(j,target-coins[j]))
                memo[(target)]=temp
            return  memo[(target)]
        res =fn(0,amount) 
        return res if res!=float("inf") else -1