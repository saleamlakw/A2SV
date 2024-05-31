class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        xor=0
        result=0
        count=Counter()
        count[0]+=1
        for ele in word:
            idx=ord(ele)-ord("a")
            xor^=(1<<idx)
            result+=count[xor]
            for i in range(10):
                result+=count[xor^(1<<i)]
            count[xor]+=1
        return result

