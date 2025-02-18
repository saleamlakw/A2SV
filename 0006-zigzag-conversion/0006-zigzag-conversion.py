class Solution(object):
    def convert(self, s, numRows):
        bukets = [[] for _ in range(numRows)]
        turn = True
        idx = 0
        if numRows == 1:
            return s
        
        for char in s:
            if turn:
                bukets[idx].append(char)
                idx += 1
                if idx >= numRows:
                    idx = numRows - 2
                    turn = False
            else:
                bukets[idx].append(char)
                idx -= 1 
                if idx < 0:
                    idx = 1
                    turn = True
       
        for i in range(len(bukets)):
            bukets[i] = "".join(bukets[i])
        return "".join(bukets)



                


        