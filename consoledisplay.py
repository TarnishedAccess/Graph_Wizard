import pandas as pd

class ConsoleDisplay:

    @staticmethod
    def display_matrix_ow(nodes):
        labels = [str(node) for node in nodes.values()]
        matrix = [['-' for _ in range(len(nodes))] for _ in range(len(nodes))]

        for i, node in enumerate(nodes.values()):
            for connection, weight in node.connections:
                j = labels.index(str(connection))
                matrix[i][j] = weight

        df = pd.DataFrame(matrix, columns=labels, index=labels)
        print(df)
