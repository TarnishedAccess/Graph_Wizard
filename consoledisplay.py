import pandas

class ConsoleDisplay:

    def display_matrix_ow(nodes):
        labels = [str(node) for node in nodes.values()]
        matrix = [[0 for _ in range(len(nodes))] for _ in range(len(nodes))]

        for i, node in enumerate(nodes.values()):
            for connection in node.connections:
                j = labels.index(str(connection))
                matrix[i][j] = 1

        df = pandas.DataFrame(matrix, columns=labels, index=labels)
        print(df)
