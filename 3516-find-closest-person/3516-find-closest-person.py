class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        disX = abs(z-x)
        disY = abs(z-y)

        if disX == disY:
            return 0
        elif disX < disY:
            return 1
        else:
            return 2
            