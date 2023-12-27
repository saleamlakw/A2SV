class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        mx=float("-inf")
        re=0
        for i in range(len(nums)-1):
            if nums[i] >nums[i+1]:
                re+=1
        if re>1:
            return False
        else:
            for i in range(len(nums)-1):
                if nums[i] >nums[i+1]:
                    if min(nums[i+1:])<mx:
                        if i+2<len(nums):
                             if min(nums[i+2:])<nums[i]:
                                return False
                        else:
                            return True

                else:
                    mx=max(mx,nums[i])
        return True


