class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ps = [[0]*27]
        for i in range(len(s)):
            temp = ps[-1][:]
            temp[ord(s[i])-ord("a")]+=1
            ps.append(temp)
    
        ans = 0
        def compute(right,left):
          
            col = 0
            for i in range(27):
                col += ((right[i] - left[i])>=1)
           
            return col
        all = set(s)
        for i in range(97,97+27):
            if chr(i) in all:

                l = s.index(chr(i))
                r = s.rindex(chr(i))
                if l!= r:
                    ans += compute(ps[r],ps[l+1])
        return ans