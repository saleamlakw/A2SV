class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        re=""
        spaces.reverse()
        for i in range(len(s)):
            while spaces and spaces[-1]==i:
                re+=" "
                spaces.pop()
            re+=s[i]
        while spaces:
                re+=" "
                spaces.pop()
        return re
