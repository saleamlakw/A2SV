class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        mini=0
        maxi=len(s)
        result=[]
        for i in s:
            if i=="I":
                result.append(mini)
                mini+=1
            else:
                result.append(maxi)
                maxi-=1
        return result+[mini]
        