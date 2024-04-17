class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=Counter(words)
        heap=[]
        for ele in freq:
            heappush(heap,((-1*freq[ele]),ele))
        print(heap)
        result=[]
        while k:
            val,w=heappop(heap)
            result.append(w)
            k-=1
        return result
