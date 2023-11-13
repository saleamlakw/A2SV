class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result=[]
        i,j=0,0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        if i<m:
            result+=nums1[i:]
        if j<n:
            result+=nums2[j:]
        for k in range(len(nums1)):
            nums1[k]=result[k]
        