class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort() #---nlogn
        nums2.sort() #---nlogn
        p1=p2=0
        result=[]  #----len(min(n,m))
        while p1<len(nums1) and p2<len(nums2): #--n+m
            if nums1[p1]==nums2[p2]:
                if result and result[-1]==nums1[p1]:
                    pass
                else:
                    result.append(nums1[p1])
                p1+=1
            elif nums1[p1]>nums2[p2]:
                p2+=1
            else:
                p1+=1
        return result