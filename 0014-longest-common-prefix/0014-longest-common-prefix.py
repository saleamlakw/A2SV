class Solution:
    def sim(self,left,right):
        re=""
        i=0
        while i<len(left) and i<len(right):
            if left[i]==right[i]:
                re+=left[i]
            else:
                return re
            i+=1
        return re
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        left=strs[0]
        for i in range(1,len(strs)):
            right=strs[i]
            left=self.sim(left,right)
            if not left:
                return ""
        return left
        