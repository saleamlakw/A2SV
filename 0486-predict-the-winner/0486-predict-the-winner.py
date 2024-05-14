class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo={}
        def dp(l,r,turn):
            if l>r:
                return 0
            if (l,r,turn) not in memo:
                if turn:
                    a=nums[l]+dp(l+1,r,0)
                    b=nums[r]+dp(l,r-1,0)
                    memo[(l,r,turn)]=max(a,b)
                else:
                    a=-nums[l]+dp(l+1,r,1)
                    b=-nums[r]+dp(l,r-1,1)
                    memo[(l,r,turn)]=min(a,b)
            return memo[(l,r,turn)]
        return True if dp(0,len(nums)-1,1) >=0 else False