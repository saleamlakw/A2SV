class Solution(object):
    def pivotArray(self, nums, pivot):
        large=[]
        re=deque()
        for num in nums[::-1]:
            if num<pivot:
                re.appendleft(num)
            elif num==pivot:
                re.append(num)
            else:
                large.append(num)
        for r in large[::-1]:
            re.append(r)
        return list(re)
            
        