class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:  
        result=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    result.append([list1[i],i+j])
        if re:
            result.sort(key=lambda x:x[1])
            return [x[0] for x in result if x[1]==result[0][1]]
        return re

        