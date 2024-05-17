class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo=[-1]*len(questions)
        def dp(i):
            if i>=len(questions):
                return 0
            if memo[i]==-1:

                take=questions[i][0]+dp(i+1+questions[i][1])
                nottake=dp(i+1)
                memo[i]=max(take,nottake)
            return  memo[i]
        return dp(0)