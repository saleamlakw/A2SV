class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ss=list(set(nums))
        ss.sort()
        mi=min(ss)

        cc=Counter(nums)
        re=0
        for k in range(len(ss)-1,-1,-1):
            # print(k)
            if ss[k]==mi:
                break
            re+=cc[ss[k]]
            if k-1>=0:
                cc[ss[k-1]]+=cc[ss[k]]
            # print(cc)
        return re
            