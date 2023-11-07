class Solution(object):
    def runningSum(self, nums):
        prefixSum=[]
        for num in nums:
            if prefixSum:
                prefixSum.append(prefixSum[-1]+num)
            else:
                prefixSum.append(num)
        return prefixSum
#intialize an array to keep track of the cummulative sum
#i will iterate through nums array and append the cumulative sum upto that element and the element itsef into the prefixsum array
#return the prefixsum array