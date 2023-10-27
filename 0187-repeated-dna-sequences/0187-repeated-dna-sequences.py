class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap=Counter()
        l=0
        for r in range(len(s)):
            while r-l>9:
                l+=1
            hashmap[s[l:r+1]]+=1
            # print(window)
            # print(hashmap)
        return [k for k in hashmap if hashmap[k]>1]
                
            