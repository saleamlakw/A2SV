class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        l,r=len(players)-1,len(trainers)-1
        trainers.sort()
        players.sort()
        ans=0
        while l>=0 and r>=0:
            if trainers[r]>=players[l]:
                ans+=1
                r-=1
                l-=1
            elif players[l]>trainers[r]:
                l-=1
        return ans
