class Node:
    def __init__(self, label):
        self.label = label
        self.connections = []

    def add_connection(self, node, weight):
        self.connections.append((node, weight))

    def __str__(self):
        return self.label