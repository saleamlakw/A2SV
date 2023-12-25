
class Solution:
              def largestPerimeter(self, nums):
                            nums.sort(reverse=True)
                            for r in range(len(nums)-2):
                                          if(nums[r+2]+nums[r+1])>nums[r]:
                                                          return (nums[r]+nums[r+1]+nums[r+2])
                            return 0       