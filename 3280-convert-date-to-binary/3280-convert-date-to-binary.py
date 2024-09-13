class Solution:
    def convertDateToBinary(self, date: str) -> str:
        d=date.split("-")
        ans=[]
        for num in d:
            ans.append(bin(int(num))[2:])
        return "-".join(ans)