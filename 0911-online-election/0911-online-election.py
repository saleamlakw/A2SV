class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons =persons
        self.times=times
        self.count=Counter()
        self.count[self.persons[0]]+=1
        self.winner=[[self.persons[0],self.count[self.persons[0]]]]
        for i in range(1,len(self.persons)):
            self.count[self.persons[i]]+=1
            if self.count[self.persons[i]]>=self.winner[-1][-1]:
                self.winner.append([self.persons[i],self.count[self.persons[i]]])
            else:
                self.winner.append(self.winner[-1])
        print(self.winner)

    def q(self, t: int) -> int:
        ind=bisect_right(self.times,t)
        
        if ind-1>=0:
            ind-=1
        return self.winner[ind][0]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)