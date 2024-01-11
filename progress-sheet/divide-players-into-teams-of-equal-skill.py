class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r=0,len(skill)-1
        ch=skill[r]+skill[l]
        result=0
        while l<r:
            if (skill[r]+skill[l])!=ch:
                return -1
            else:
                result+=(skill[r]*skill[l])
            l+=1
            r-=1
        return result