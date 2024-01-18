class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        ma=float("-inf")
        r=len(tasks)-1
        for i in processorTime:
            k=4
            while r>=0 and k:
                ma=max(ma,i+tasks[r])
                k-=1
                r-=1
        return ma

        