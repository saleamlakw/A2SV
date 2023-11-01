class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                answer[stack.pop()]=i-stack[-1]
            stack.append(i)
        return answer