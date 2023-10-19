class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            mi=i
            for j in range(i,len(heights)):
                if heights[mi]<heights[j]:
                    mi=j
            heights[mi],heights[i]=heights[i],heights[mi]
            names[mi],names[i]=names[i],names[mi]
        return names
                