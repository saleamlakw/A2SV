class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hashmap=Counter()
        for r in arr:
            hashmap[r]+=1
            if  hashmap[r]>((len(arr)*25)/100):
                return r