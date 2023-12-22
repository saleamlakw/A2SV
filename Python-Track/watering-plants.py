class Solution:
    def wateringPlants(self, plants, capacity):
        plants=[capacity]+plants
        re=0
        for i in range(0,len(plants)-1):
            # print(plants[i+1],plants[0])
            if plants[i+1]<=plants[0]:
                re+=1
                plants[0]-=plants[i+1]
                # print("re",re)
            else:
                # print(plants[i+1],plants[0])
                re+=2*i+1
                plants[0]=capacity
                plants[0]-=plants[i+1]
                # print("re",re)
        return re
