class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cc=Counter()
        zeros=[]
        ones=[]
        mat=set()
        for s in matches:
            mat.add(s[0])
            mat.add(s[1])
        for r in matches:
            cc[r[1]]+=1
        for i in mat:
            if cc[i]==0:
                zeros.append(i)
            elif cc[i]==1:
                ones.append(i)
        return [sorted(zeros),sorted(ones)]