class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        from collections import defaultdict,deque
        res=0
        ch=deque()
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
            ch.append(i)
            while hashmap[0]>1:
                hashmap[ch.popleft()]-=1
            # print(ch)
            res=max(res,len(ch))
        return res-1
            
            