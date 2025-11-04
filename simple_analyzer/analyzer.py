class Analyzer():
    def __init__(self):
        self.data = []
    
    def add_number(self, n):
        self.data.append(n)
    
    def even_count(self):
        sum = 0
        for elem in self.data:
            sum += 1 - elem % 2
        return sum

    def odd_count(self):
        sum = 0
        for elem in self.data:
            sum += elem % 2
        return sum
    
    def highest_number(self):
        if(len(self.data) > 0):
            h = self.data[0]
            for elem in self.data:
                h = max(h, elem)
            return h
    
    def increasing_pairs(self):
        res = 0
        if(len(self.data) > 1):
            for i in range(len(self.data) - 1):
                if(self.data[i] < self.data[i + 1]):
                    res += 1
        return res
    
    def average_number(self):
        res = 0
        for elem in self.data:
            res += elem
        if(len(self.data) > 0):
            res /= len(self.data)
        return res
    
    def max_min_diff(self):
        if(len(self.data) > 0):
            mmax = self.data[0]
            mmin = self.data[0]
            for elem in self.data:
                mmax = max(elem, mmax)
                mmin = min(elem, min)
            return mmax - mmin
    


