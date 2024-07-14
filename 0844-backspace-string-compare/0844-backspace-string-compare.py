class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss=[]
        tt=[]
        for ele in s:
            if ele =="#":
                if ss:ss.pop()
            else:
                ss.append(ele)

        for ele in t:
            if ele=="#":
                if tt:tt.pop()
            else:
                tt.append(ele)

        return tt==ss