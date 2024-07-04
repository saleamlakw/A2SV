class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        res=0
        for rabbit in count:
            res+=ceil(count[rabbit]/(rabbit+1))*(rabbit+1)
        return res
             