class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1=Counter(nums1)
        count2=Counter(nums2)
        result=[]
        
        
        for ele in count1:
            result.extend(min(count1[ele],count2[ele])*[ele])
        return result
        