class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result=[]
        def fn(st,i):
            if i==len(s):
                result.append(st)
                return 
            if s[i].isdigit():
                fn(st+s[i],i+1)
            else:
                fn(st+s[i].lower(),i+1)
                fn(st+s[i].upper(),i+1)
        fn("",0)
        return result
