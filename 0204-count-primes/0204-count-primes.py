class Solution:
    def countPrimes(self, n: int) -> int:
            arr=[1]*n
            if n<2:
                return 0
            arr[0]=arr[1]=0
            for i in range(2,n):
                if arr[i] and i*i<n:
                    for j in range(i*i,n,i):
                        arr[j]=0
            result=0
            for k in arr:
                if k:
                    result+=1
            return result