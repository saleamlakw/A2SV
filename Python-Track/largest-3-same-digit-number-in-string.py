class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l=0
        re="0"
        hashmap=Counter()
        for r in range(len(num)):
            hashmap[num[r]]+=1
            while r-l+1>3:
                hashmap[num[l]]-=1
                if hashmap[num[l]]==0:
                    hashmap.pop(num[l])
                l+=1
            if r-l+1==3 and len(hashmap)==1:
                if int(re[0])<=int(num[l]):
                    re="".join(num[l:r+1])
        return re if len(re)==3 else ""
                
                
                