class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot=sum(rolls)
        rem=((len(rolls)+n)*mean)-tot
        k=rem//n
        if 0<k<=6 and 0<k+(rem%n)<=6:
            ans=[k]*(n-1)
            ans+=[k+(rem%n)]
            return ans
        else:
            return []