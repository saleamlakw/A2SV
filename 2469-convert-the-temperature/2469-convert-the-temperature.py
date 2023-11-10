class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=celsius + 273.15
        Fahrenheit=celsius * 1.80 + 32.00
        return [kelvin,Fahrenheit]