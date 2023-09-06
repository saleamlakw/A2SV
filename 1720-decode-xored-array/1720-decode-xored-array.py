class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        re=[]
        re.append(first)
        for i in range(len(encoded)):
            re.append(first^encoded[i])
            first=first^encoded[i]
        return re
        