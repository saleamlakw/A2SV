class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        def build_prefix_table(pattern):
            table, j = [0] * len(pattern), 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = table[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                table[i] = j
            return table
        lps = build_prefix_table(goal)
        pattern = s+s
        j=0
        for i in range(len(pattern)):
            while j>0 and goal[j]!=pattern[i]:
                j = lps[j-1]
            if pattern[i] == goal[j]:
                j+=1
            if j==len(goal):
                return True
        return False 

