class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            ps1=[1]
            for ele in nums:
                ps1.append(ps1[-1]*ele)
            ps1.append(1)
            ps2=[1]
            for el in nums[::-1]:
                 ps2.append(ps2[-1]*el)
            ps2.append(1)
            ps2=ps2[::-1]
            result=[]
            for i in range(1,len(ps1)-1):
                re=ps1[i-1]*ps2[i+1]
                result.append(re)
            return (result)

