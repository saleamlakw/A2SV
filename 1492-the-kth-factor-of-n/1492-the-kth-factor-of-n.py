class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        div=[]
        for i in range(1,int(pow(n,0.5))+1):
            if n%i==0:
                div.append(i)
                dd=n//i
                if dd!=i:
                    div.append(dd)
        div.sort()
        # print(div)
        if k-1<len(div):
            return div[k-1]
        else:
            return -1

        
        