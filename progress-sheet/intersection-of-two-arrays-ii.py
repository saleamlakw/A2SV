class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        c1=Counter(nums1)
        c2=Counter(nums2)
        for i in c2:
            if i in c1:
                for _ in range(min(c1[i],c2[i])):
                    result.append(i)
        return result