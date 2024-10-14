class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i in range(len(nums)):
            heappush(max_heap , -nums[i])
        ans=0
        while k:
            poped = -1*heappop(max_heap)
            ans += poped
            heappush(max_heap ,-1*ceil(poped/3))
            k -= 1
        return ans