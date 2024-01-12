class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r= 0,len(height) - 1
        mx = float("-inf")
        while l < r:
            
            v = (r - l) * min(height[l],height[r])
            mx = max(mx,v)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        return mx
