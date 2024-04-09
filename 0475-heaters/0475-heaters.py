class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def bs(arr,target):
            ind=bisect_left(arr,target)
            # print([ind,target,arr])
            re=float("inf")
            if ind<len(arr):
                re=min(re,abs(arr[ind]-target))
            if ind-1>=0:
                re=min(re,abs(arr[ind-1]-target))
            return re
        heaters.sort()
        result=float("-inf")
        for i in range(len(houses)):
            result=max(result,bs(heaters,houses[i]))
        return result

           