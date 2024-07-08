class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=list(range(1,n+1))
        start=0
        des=(start+(k-1))%len(arr)
        while len(arr)!=1:
            des=(start+(k-1))%len(arr)
            arr.pop(des)
            start=des
        return arr[0]
