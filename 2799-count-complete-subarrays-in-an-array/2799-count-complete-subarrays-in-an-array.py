class Solution(object):
    def countCompleteSubarrays(self, nums):
        answer = 0
        numberOfDistnict = len(set(nums))
        count = defaultdict(int) #o(n)
        left = right = 0

        for right in range(len(nums)):
            count[nums[right]] += 1
            while len(count) == numberOfDistnict:
                answer += (1 + len(nums) - (right + 1))
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                left += 1

        return answer
