class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less=[]
        equal=[]
        greater=[]
        for r in nums:
            if r<pivot:
                less.append(r)
            elif  r>pivot:
                greater.append(r)
            else:
                equal.append(r)
        return less+equal+greater