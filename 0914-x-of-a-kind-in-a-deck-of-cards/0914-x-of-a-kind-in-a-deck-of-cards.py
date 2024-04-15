class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        frequency=Counter(deck)
        gcd_=frequency[deck[0]]

        for ele in set(deck):
            gcd_=math.gcd(gcd_,frequency[ele])
            
        return gcd_>1
    


