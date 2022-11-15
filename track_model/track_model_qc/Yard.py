

class Yard():
    def __init__(self):
        self.lines_connections = dict()

    def add_connection(self, line, block):
        if line in self.lines_connections:
            self.lines_connections[line].append(block)
        else:
            self.lines_connections[line] = [block]
    
    def get_connections(self, line):
        return self.lines_connections[line]
            