class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join([str(1-int(i)) for i in bin(num)[2:]]),2)
