class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result=[]
        for i in range(len(l)):
            ch=nums[l[i]:r[i]+1]
            if len(ch)<2:
                result.append(False)
            else:
                re=True
                ch.sort()
                c=ch[1]-ch[0]
                for k in range(len(ch)-1):
                    if ch[k+1]-ch[k]!=c:
                        re=False
                        break
                result.append(re)
        return result
