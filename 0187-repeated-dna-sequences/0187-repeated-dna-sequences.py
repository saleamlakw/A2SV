class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap=Counter()
        window=deque()
        for r in range(len(s)):
            window.append(s[r])
            while len(window)>10:
                window.popleft()
            hashmap["".join(list(window))]+=1
            # print(window)
            # print(hashmap)
        return [k for k in hashmap if hashmap[k]>1]
                
            