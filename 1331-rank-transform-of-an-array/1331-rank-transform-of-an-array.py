class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap=Counter()
        rank=1
        for ele in sorted(arr):
            if ele not in hashmap:
                hashmap[ele]=rank
                rank+=1

        return [hashmap[i] for i in arr]
