class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        re=[]
        ma=max(candies)
        for i in candies:
            if (i+extraCandies)>=ma:
                re.append(True)
            else:
                re.append(False)
        return re
        