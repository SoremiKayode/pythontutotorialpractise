import math
class stat:
    def __init__(self, data_array:list):
        self.data = data_array
    def mean(self):
        self.m = int(sum(self.data) / len(self.data))
        return self.m
    def mode(self):
        frequently = [self.data.count(x) for x in self.data]
        occur = frequently.index(max(frequently))
        return self.data[occur]

    def standard_deviation(self):
        temp_number = []
        for number in self.data :
            temp_number.append((number - self.m) ** 2)
        self.std = sum(temp_number) / len(self.data)
        return math.sqrt(self.std)
        



c = stat([45, 6, 7, 6, 45, 8, 7, 6, 6, 5, 7])

print(c.mode())
print(c.mean())
print(c.standard_deviation())