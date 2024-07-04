class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance=defaultdict()
        for i in range(len(s)):
            last_occurance[s[i]]=i
        
        res=[]
        count=Counter(s)
        max_index=0
        l=0
        for i in range(len(s)):
            count[s[i]]-=1
            if count[s[i]]==0 and i>=max_index:
                res.append((i-l)+1)
                l=i+1
            max_index=max(max_index,last_occurance[s[i]])
        return res