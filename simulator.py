
class Simulator:
    def __init__(self):             
        self.m1 = 0.0
        self.m2 = 0.0
        self.m3 = 0.0
        self.light = 0.0

        self.m1_kw = 200.0
        self.m2_kw = 200.0
        self.m3_kw = 200.0
        self.light_kw = 10.0
        self.total_kw = 0.0

        self.array = []

        self.sma_array = []
        self.sma_length = 20
        self.sma_index = 0

        self.create_array(self.sma_length)

    def clear(self):
        self.create_array(self.sma_length)
        
    def create_array(self, length):
        for i in range(length):
            self.sma_array.append(0.0)
        self.sma_length = length

    def sma(self, value):
        self.sma_array[self.sma_index % self.sma_length] = value
        self.sma_index += 1
        total = 0
        for v in self.sma_array:
            total += v
        #print self.sma_array
            
        return total/float(self.sma_length )

    def add_data(self, data):
        
        self.m1 = data[0] * self.m1_kw
        self.m2 = data[1] * self.m2_kw
        self.m3 = data[2] * self.m3_kw
        self.light = data[3] * self.light_kw
        self.total_kw = self.m1 + self.m2 + self.m3 + self.light
        val = self.sma(self.total_kw)
        return val 
