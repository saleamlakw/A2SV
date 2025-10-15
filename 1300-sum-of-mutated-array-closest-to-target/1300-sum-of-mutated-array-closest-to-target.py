class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()

        running_sum = 0

        ans = [0,float(inf)]
        idx = 0
        for val in range(arr[-1]+1):
            while idx < len(arr) and arr[idx] <= val:
                running_sum += val
                idx += 1
    
            remain = len(arr) - idx
            current_sum = running_sum +  (remain * val)
            difference = abs(target - current_sum)

          
            if ans[-1] > difference:
                ans[0] = val
                ans[-1] = difference
            
        return ans[0]


        