class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cc=Counter()
        l=0
        re=0
        for r in range(len(s)):
            cc[s[r]]+=1
            while r-l+1>len(cc):
                cc[s[l]]-=1
                if cc[s[l]]==0:
                    cc.pop(s[l])
                l+=1
            if r-l+1==len(cc):
                re=max(re,r-l+1)
        return re
