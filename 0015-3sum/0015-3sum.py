class Solution:
   def threeSum(self, nums):
        result=set()
        nums.sort()
        # print(nums)
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while r>l:
               
                sum_=nums[i]+nums[l]+nums[r]
                # print(sum_,nums[i],nums[l],nums[r])
                if sum_<0:
                    l+=1
                elif sum_>0:
                    r-=1
                else:
                    result.add(tuple(sorted(list([nums[i],nums[l],nums[r]]))))
                    while r>l and nums[l]==nums[l+1]:
                        l+=1
                    while r>l and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return list(result)
                


            
            
        return result

            
            

