class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(word , pattern):
            if len(word)!=len(pattern):
                return False
            match={}
            for i in range(len(word)):
                match[pattern[i]]=word[i]
            count=Counter(match.values())
            if max(count.values())>1:
                return False 
            res=[match[char] for char in pattern]
            print(word,pattern,res,match)
            return "".join(res)==word
        ans=[]
        for word in words:
            if check(word,pattern):
                ans.append(word)
        return ans
           