# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
      l=1
      r=n
      re=0
      while l<=r:
          mid=(l+r)//2
          if not isBadVersion(mid):
              l=mid+1
          else:
              re=mid
              r=mid-1
      return re
