class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        a=defaultdict(list)
        op=0
        for i in nums:
            # print(a)
            if i in a and a[i]:
                    a[i].pop()
                    op+=1
            else:
                a[k-i].append(i)
        return op

        



        
