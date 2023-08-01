class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
            counts=Counter()
            cur_sum=0
            result=0
            for i in nums:
                cur_sum+=i
                if cur_sum%k==0: result+=1
                result+=counts[cur_sum%k]
                counts[cur_sum%k]+=1
            return result
                
            
    
        