class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums=[]

        for i in range(len(s)):
            nums.append(str(ord(s[i])-96))
        nums="".join(nums)
        while k:
            # print(nums)
            tot=sum(list(map(int,list(nums))))
            nums=str(tot)
            k-=1
        return tot

