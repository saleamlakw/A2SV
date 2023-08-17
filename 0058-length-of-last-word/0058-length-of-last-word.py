class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        al=s.split()
        return len(al[-1])
        