class LineInfo():
    def __init__(self, line_name: str):
        self.line_name = line_name
        self.throughput = 0
        
    def setThroughput(self, throughput):
        self.throughput = throughput

    def get_throughput(self):
        return self.throughput