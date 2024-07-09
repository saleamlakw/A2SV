class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total=0
        start=0
        
        for arrival,time in customers:
            start=max(arrival,start)+time
            total+=start-arrival
        return total/len(customers)    
            