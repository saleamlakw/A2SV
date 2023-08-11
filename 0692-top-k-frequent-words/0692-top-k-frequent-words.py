class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return heapq.nlargest(k,sorted(set(words)),key=lambda x: (words.count(x),))
        