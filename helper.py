class Helper:
    
    @staticmethod
    def taille(nodes):
        return sum(len(node.connections) for node in nodes.values())

    @staticmethod
    def ordre(nodes):
        return len(nodes)
