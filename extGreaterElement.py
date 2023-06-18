class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        result=[]
        ch=[-1]*(max(nums2)+1)
        for i,val in enumerate(nums2):
            while stack and nums2[stack[-1]]<val:
                ch[nums2[stack.pop()]]=val
            stack.append(i)
        for k in nums1:
            result.append(ch[k])
        return result



        
