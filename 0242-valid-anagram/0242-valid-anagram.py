class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)

        for ele in countS:
            if countS[ele] != countT[ele]:
                return False
        
        for ele in countT:
            if countT[ele] != countS[ele]:
                return False
        return True