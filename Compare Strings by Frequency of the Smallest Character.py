class Solution:
    from bisect import bisect_right
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
       f=lambda x:x.count(min(x))
       w=sorted(list(map(f,words)))
       return [len(w)-bisect_right(w,i) for i in map(f,queries)]
