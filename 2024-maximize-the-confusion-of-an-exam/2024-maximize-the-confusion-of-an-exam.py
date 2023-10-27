class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        window=deque()
        hashmap=Counter()
        res=0
        for r in answerKey:
            window.append(r)
            hashmap[r]+=1
            # print(hashmap)
            while hashmap["T"]>k and hashmap["F"]>k:
                hashmap[window.popleft()]-=1
            # print(window)
            res=max(res,len(window))
        return res