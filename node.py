class Node:
    def __init__(self, label):
        self.label = label
        self.connections = []

    def add_connection(self, node):
        self.connections.append(node)

    def __str__(self):
        return self.label