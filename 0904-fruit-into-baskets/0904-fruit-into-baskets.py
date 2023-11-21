class Solution(object):
    def totalFruit(self, fruits):
        l=0
        result=-1
        countOfFruits=Counter()
        for r in range(len(fruits)):
            countOfFruits[fruits[r]]+=1  
            while len(countOfFruits)>2:
                countOfFruits[fruits[l]]-=1
                if countOfFruits[fruits[l]]==0:
                    countOfFruits.pop(fruits[l])
                l+=1
            result=max(result,r-l+1)
        return result