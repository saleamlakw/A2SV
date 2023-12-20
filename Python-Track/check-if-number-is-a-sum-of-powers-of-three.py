class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n!=1:
            if n%3>1:
                return False
            n//=3
        return True