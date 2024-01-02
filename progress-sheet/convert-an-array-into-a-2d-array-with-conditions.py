class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hashmap=Counter(nums)
        index_map=Counter()
        matrix=[[]for _ in range(max(hashmap.values()))]
        for i in range(len(nums)):
            matrix[index_map[nums[i]]].append(nums[i])
            index_map[nums[i]]+=1
        return matrix
