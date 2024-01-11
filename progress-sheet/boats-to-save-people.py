class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        re=0
        people.sort()
        l=0
        r=len(people)-1
        while l<=r:
            if people[l]+people[r]<=limit:
                re+=1
                l+=1
                r-=1
            else:
                re+=1
                r-=1
        return re