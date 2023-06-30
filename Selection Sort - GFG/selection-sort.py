#User function Template for python3

class Solution: 
    def select(self, arr, i):
        m=i
        for k in range(i+1,len(arr)):
            if arr[m]>arr[k]:
                m=k
        return m
    def selectionSort(self, arr,n):
        for i in range(n):
            v=self.select(arr,i)
            if i!=v:
                arr[v],arr[i]=arr[i],arr[v]
                
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends