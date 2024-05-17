class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
            n=len(questions)
            dp=[0]*n
            for i in range(n-1,-1,-1):
                take=dp[i+1+questions[i][1]] if (i+1+questions[i][1])<n else 0
                nottake=dp[i+1] if (i+1)<n else 0
                dp[i]=max(questions[i][0]+take,nottake)
            # print(dp)
            return  dp[0]
        # def dp(i):
        #     if i>=len(questions):
        #         return 0
        #     if memo[i]==-1:
        #         take=questions[i][0]+dp(i+1+questions[i][1])
        #         nottake=dp(i+1)
        #         memo[i]=max(take,nottake)
        #     return  memo[i]
        # return dp(0)