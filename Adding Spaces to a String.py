class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        li=[]
        spaces=sorted(spaces)[::-1]
        for i,v in enumerate(s):
            if spaces and  i ==spaces[-1]:
                li.append(" "+v)
                spaces.pop()

            else:
                li.append(v)
        return ("".join(li))
