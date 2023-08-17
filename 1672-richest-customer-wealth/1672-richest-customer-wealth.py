class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ma=float("-inf")
        for i in accounts:
            ma=max(ma,sum(i))
        return ma
        