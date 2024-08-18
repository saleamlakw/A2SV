class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers = [0] * n
        uglyNumbers[0] = 1
        i2 = i3 = i5 = 0
        
        nextMultipleOf2 = 2
        nextMultipleOf3 = 3
        nextMultipleOf5 = 5
        
        for i in range(1, n):
            nextUglyNumber = min(nextMultipleOf2, nextMultipleOf3, nextMultipleOf5)
            uglyNumbers[i] = nextUglyNumber
            
            if nextUglyNumber == nextMultipleOf2:
                i2 += 1
                nextMultipleOf2 = uglyNumbers[i2] * 2
            if nextUglyNumber == nextMultipleOf3:
                i3 += 1
                nextMultipleOf3 = uglyNumbers[i3] * 3
            if nextUglyNumber == nextMultipleOf5:
                i5 += 1
                nextMultipleOf5 = uglyNumbers[i5] * 5
        
        return uglyNumbers[n - 1]