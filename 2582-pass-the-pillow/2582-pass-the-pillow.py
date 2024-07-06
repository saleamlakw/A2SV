class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        turn = True
        index=1
        while time:
            if turn:
                index+=1
            else:
                index-=1
            if index == n:
                turn = False
            if index==1:
                turn = True
            time-=1
        return index
                
            