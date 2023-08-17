class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            left=""
            j=i
            while j<len(haystack) and len(left)!=len(needle):
                left+=haystack[j]
                j+=1
            if left==needle:
                return i
        return -1
            