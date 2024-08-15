class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0


        for i in range(len(bills)):
            if bills[i]==5:
                five+=5
            elif bills[i]==10:
                if five:
                    five-=5
                else:
                    return False
                ten+=10
            else:
                if ten:
                    ten-=10
                    bills[i]-=10
                if bills[i]>five+5:
                    return False
                else:
                    five-=(bills[i]-5)
        return True
