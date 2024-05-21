class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1]-stones[0]>1:
            return False

        st=set(stones)
        memo={}
        def dp(k,cur):
            if cur==stones[-1]:
                return True
            # print(k,cur)
            if (k,cur) not in memo:
                re=False
                if cur in st:
                    re = re or dp(k,cur+k) 
                    re=re or (dp(k-1,cur+k-1) if k-1>0 else False)
                    re=re or dp(k+1,cur+k+1)
                memo[(k,cur)]=re
            return memo[(k,cur)]
        return dp(1,stones[1])



            