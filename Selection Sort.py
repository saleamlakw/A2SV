#User function Template for python3
class Solution: 
    def select(self, arr, i):
        m=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[m]:
                m=j
        return m
    def selectionSort(self, arr,n):
        for k in range(n):
            m=self.select(arr,k)
            arr[k],arr[m]=arr[m],arr[k]
        return arr
