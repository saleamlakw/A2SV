class Solution(object):
    def rearrangeArray(self, nums):
        positive=[] #--> n/2
        negative=[] #--> #n/2

        for num in nums:       #---n
            if num>0:
                positive.append(num)
            else:
                negative.append(num)

        p1=p2=0 #1
        index=0 #1
        while p1<len(positive) and p2<len(negative):#---- n/2->n
            nums[index]=positive[p1]
            nums[index+1]=negative[p2]
            p1+=1
            p2+=1
            index+=2
        return nums