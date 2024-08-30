class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(arr):
            low=0
            high=len(arr)-1

            while low<=high:
                mid=(low+high)//2
                if arr[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return low if low <len(arr) and 0<=low and  arr[low]==target else -1
        def upper_bound(arr):
            low=0
            high=len(nums)-1

            while low<=high:
                mid=(low+high)//2
                if arr[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return high if high <len(arr) and 0<=high and arr[high]==target else -1

        return [lower_bound(nums),upper_bound(nums)]
