class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ch=[0]*len(temperatures)
        stack=[]
        for i,val in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<val:
                poped=stack.pop()
                ch[poped]=(i-poped)
            stack.append(i)
        return ch
        
        




        

