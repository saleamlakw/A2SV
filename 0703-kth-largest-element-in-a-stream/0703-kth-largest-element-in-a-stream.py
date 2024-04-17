class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        heapify(self.nums)
        while len(self.nums)>self.k:
            heappop(self.nums)
    def add(self, val: int) -> int:
        # print(self.nums)
        if len(self.nums)<self.k:
            heappush(val)
        else:
            if val>self.nums[0]:
                heapreplace(self.nums,val)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)