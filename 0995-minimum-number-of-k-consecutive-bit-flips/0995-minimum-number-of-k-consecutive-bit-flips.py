class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ans=0
        flip=0
        tempk=k
        start=deque()
        for i in range(len(nums)):
            # print(i,nums[i],flip,tempk)
            if nums[i]==0:
                if flip%2==0:
                    if len(nums)-i<k:
                        return -1
                    flip+=1
                    start.append(i)
            else:
                if flip%2!=0:
                    if len(nums)-i<k:
                        return -1
                    flip+=1
                    start.append(i)
            if flip:
                tempk-=1
            if tempk==0:
                if flip:
                    ans+=1
                    flip-=1
                    if start:
                        start.popleft()
                    if start:
                        tempk=(k-(i-start[0]+1))
                    else:
                        tempk=k
        return ans
