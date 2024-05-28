class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def countSmaller(nums) :
            nums=list(enumerate(nums))
            res=[0]*len(nums)
            def merge_sort(l,r):
                if l>=r:
                    return 
                m=(l+r)//2
                merge_sort(l,m)
                merge_sort(m+1,r)
                merge(l,m,r)
                
            def merge(l,m,r):
                left=l
                right=m+1
                temp=[]
                while left<=m and right<=r:
                    if nums[left][1]<=nums[right][1]:
                        res[nums[left][0]]+=(right-m-1)
                        temp.append(nums[left])
                        left+=1
                    else:
                        temp.append(nums[right])
                        right+=1
                while left<=m:
                        res[nums[left][0]]+=(right-m-1)
                        temp.append(nums[left])
                        left+=1
                while right<=r:
                        temp.append(nums[right])
                        right+=1
                nums[l:r+1]=temp
            merge_sort(0,len(nums)-1)
            return res
        n=len(instructions)
        ordered=instructions[::-1]
        re=countSmaller(ordered)
        # print(re)
        result=0
        count=Counter(instructions)
        for i in range(n):
            # print(re[i],n-re[i]-count[ordered[i]])
            result+=min(re[i],n-i-re[i]-count[ordered[i]])
            count[ordered[i]]-=1
        return result%(10**9+7)

