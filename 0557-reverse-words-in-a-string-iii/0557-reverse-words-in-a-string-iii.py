class Solution:
    def reverseWords(self, s: str) -> str:
        re=""
        ss=s.split()
        while ss:
            re+=ss.pop()+" "
        return re[::-1].strip()
        