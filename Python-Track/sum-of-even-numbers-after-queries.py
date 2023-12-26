class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        totEven=0
        for r in nums:
            if r%2==0:
                totEven+=r
        
        result=[]
        for  val,ind in queries:
            if nums[ind]%2 != 0:
                if (nums[ind]+val)%2==0:
                    totEven+=(nums[ind]+val)
            else:
                if (nums[ind]+val)%2==0:
                    totEven+=(val)
                else:
                    totEven-=nums[ind]
            result.append(totEven)
            nums[ind]=(nums[ind]+val)
        return result
        