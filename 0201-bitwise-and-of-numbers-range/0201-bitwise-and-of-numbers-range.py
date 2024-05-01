class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count=0
        while left !=right and left!=0 and right!=0:
            left>>=1
            right>>=1
            count+=1
        return left<<count if left  and right else 0



        