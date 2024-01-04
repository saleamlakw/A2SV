class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left=False
        right=False
        mid=-1
        for i in range(1,len(arr)):
            if arr[i-1]==arr[i]:
                return False
            if arr[i-1]>arr[i]:
                mid=i
                left=True
                break
            
        # print("left",arr[:mid-1])
        # print("right",arr[mid-1:])
        if left and (arr[:mid-1]):
            for j in range(mid-1,len(arr)-1):
                if (arr[j]==arr[j+1]) or (arr[j]<arr[j+1]):
                    return False
            right=True
        return (left and right)
            
            
            
