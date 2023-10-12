class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        re={}
        num=sorted(nums)
        x=len(num)
        for i in num:
            if i not in re:re[i]=len(num)-x
            x-=1
        print(re)
        return [re[k] for k in nums ]
        
            
            