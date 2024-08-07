class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        
        for s in strs:
            dic["".join(list(sorted(s)))].append(s)
        return dic.values()