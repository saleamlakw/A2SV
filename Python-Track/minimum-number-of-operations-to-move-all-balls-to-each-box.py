class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result=[]
        for i in range(len(boxes)):
            re=0
            for j in range(len(boxes)):
                if i!=j:
                    if boxes[j]=="1":
                        re+=abs(i-j)
            result.append(re)
        return result


