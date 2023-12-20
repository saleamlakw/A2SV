class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def comp(s1,s2):
            re=""
            l=r=0
            while l<len(s1) and r<len(s2):
                if s1[l]==s2[r]:
                    re+=s1[l]
                else:
                    return re
                l+=1
                r+=1
            return re
        left=strs[0]
        for right in strs:
            left=comp(left,right)
        return  left
                