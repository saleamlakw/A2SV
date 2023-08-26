class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def maxSum(nums):
            nonlocal total
            maxSum=float('-inf')
            curSum=0
            for i in nums:
                curSum=max(0,curSum)
                curSum+=i
                maxSum=max(maxSum,curSum)
                total+=i
            return maxSum
        def minSum(nums):
            minSum=nums[0]
            cursum=0
            for j in nums:
                cursum=min(cursum+j,j)
                minSum=min(minSum,cursum)
            return minSum
        total=0
        ma_sum=maxSum(nums)
        print(ma_sum)
        mi_sum=minSum(nums)
        print(mi_sum)
        print(total,"tot")
        return max(total-mi_sum,ma_sum) if ma_sum >0 else ma_sum
        
        