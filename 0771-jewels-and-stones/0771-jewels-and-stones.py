class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        re=0
        for i in stones:
            if i in jewels:
                re+=1
        return re