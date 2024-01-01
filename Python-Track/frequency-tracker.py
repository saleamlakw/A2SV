class FrequencyTracker:

    def __init__(self):
        self.Frequency=Counter()
        self.FrequencyOfFrequency=Counter()

    def add(self, number: int) -> None:
        if number in self.Frequency:
            if  self.Frequency[number] in self.FrequencyOfFrequency:
                self.FrequencyOfFrequency[self.Frequency[number]]-=1
        self.Frequency[number]+=1
        self.FrequencyOfFrequency[self.Frequency[number]]+=1
    def deleteOne(self, number: int) -> None:
        if number in self.Frequency:
            if  self.Frequency[number] in self.FrequencyOfFrequency:
                self.FrequencyOfFrequency[self.Frequency[number]]-=1
        if number in self.Frequency:
            self.Frequency[number]-=1
            if self.Frequency[number]==0:
                self.Frequency.pop(number)
            else:
                self.FrequencyOfFrequency[self.Frequency[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return (self.FrequencyOfFrequency[frequency])


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)