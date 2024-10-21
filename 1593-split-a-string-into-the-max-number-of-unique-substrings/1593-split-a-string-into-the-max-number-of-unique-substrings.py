class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited = {}
        memo={}
        def backtrack(i):
            # print(i,visited,len(s))
            if i ==len(s):
                if  "".join(visited)==s:
                    return 0
                else:
                    return float("-inf")
            
            ans = float("-inf")
            for j in range(1,16):
                if i+j>16:
                    break
                # print(s[i:i+j])
                if s[i:i+j] not in visited:
                    visited[s[i:i+j]]=""
                    ans = max(ans,1+backtrack(i+j))
                    visited.pop(s[i:i+j])
            return ans
        return (backtrack(0))