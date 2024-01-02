class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        i=0
        result=0
        while i<len(strs[0]):
            for j in range(1,len(strs)):
                if strs[j-1][i]>strs[j][i]:
                    result+=1
                    break
            i+=1
        return result