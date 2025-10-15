class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()

        prefix_sum = list(accumulate(arr,initial = 0))
        ans , diff = 0,float(inf)

        for val in range(arr[-1]+1):
            idx = bisect_right(arr,val)
            current_sum = prefix_sum[idx] + ((len(arr)-idx)*val)
            difference = abs(current_sum - target)

            if difference < diff:
                ans = val
                diff = difference
        return ans

            


        