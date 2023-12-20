class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lex=dict(zip(order,list(range(1,len(order)+1))))
        def comp(s1,s2):
            l=r=0
            while l<len(s1) and r<len(s2):
                if lex[s1[l]]>lex[s2[r]]:
                    return False
                elif lex[s1[l]]<lex[s2[r]]:
                    return True
                l+=1
                r+=1
            if len(s1)<=len(s2):
                return True
            else:
                return False
        flag=True
        left=words[0]
        for right in words[1:]:
            flag=comp(left,right)
            left=right
            if not flag:
                return False
        return True
        