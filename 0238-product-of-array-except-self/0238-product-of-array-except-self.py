class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num=list(filter(lambda x:x!=0,nums))
        n=len(nums)-len(num)
        ma=len(num)-1
        num=num+([0]*n)
        # print(num)
        prefix_pro=[]
        pro=1
        for i in num:
            # print(pro)
            pro*=i
            prefix_pro.append(pro)
        # print(prefix_pro)
        return [prefix_pro[-1]//nums[k] if nums[k]!=0 else (prefix_pro[ma] if nums.count(0)==1 else 0)   for k in range(len(nums))]
            
        