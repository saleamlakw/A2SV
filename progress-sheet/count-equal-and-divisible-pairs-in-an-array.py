class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    result+=1
                
        return result
        
        # print(hashmap)
        # for num in frequency:
        #     if hashmap[num][0]!=-1:
        #         result+=((frequency[num]*(frequency[num]-1))//2)
        # return result
