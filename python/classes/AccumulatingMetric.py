

class AccumulatingMetric:
    def __init__(self):
        self.metric = 0
        self.counter = 0

    def add(self, value):
        # Add value to metric
        self.metric += value
        # Increase the counter by one
        self.counter += 1

    def avg(self):
        return self.metric / self.counter
    