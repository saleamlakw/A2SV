class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def check(s1,s2):
            for r in s1.lower():
                if r not in s2:
                    return False
            return True
        result=[]
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        for r in words:
            # print("r",r)
            for j in rows:
                if check(r,j):
                    result.append(r)
                    break
        return  result